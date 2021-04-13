# to login copy firefox/chrome cookies
# add to ~/.lc/leetcode/user.json
# {
#   "login": <user>,
#   "loginCSRF": "",
#   "sessionCSRF": <csrftoken>,
#   "sessionId": <LEETCODE_SESSION>,
# }
# and run leetcode user -c

import os
from dataclasses import dataclass, field
from typing import List

import clize
from utils import cammel_to_snake_case, create_folder_if_needed, get_file_name


@dataclass
class QuestionData:
    title: str = ""
    url: str = ""
    id: int = 0
    inputs: List[str] = field(default_factory=list)
    outputs: List[str] = field(default_factory=list)
    difficulty: str = ""
    function_name: str = ""
    file_name: str = ""
    code: List[str] = field(default_factory=list)


def get_question(id: int):
    data = QuestionData(id=id)
    os.system("~/Documents/leetcode-cli/leetcode-cli show " + str(id) + " > tmp.txt")
    with open("tmp.txt", "r") as f:
        for i, line in enumerate(f):
            print(line)
            if i == 0:
                data.title = " ".join(line.split()[1:])
            elif "https://leetcode" in line:
                data.url = line[:-1]
            elif "Input: " in line:
                data.inputs.append(line[7:-1])
            elif "Output: " in line:
                data.outputs.append(line[8:-1])
            elif line[0] == "*":
                words = line.split()
                if words[1] in ["Easy", "Medium", "Hard"]:
                    data.difficulty = words[1]

    os.system(
        "~/Documents/leetcode-cli/leetcode-cli show -c -l python3 "
        + str(id)
        + " > tmp.txt"
    )
    with open("tmp.txt", "r") as f:
        for line in f:
            data.code.append(line)
            if len(data.code) >= 2:
                break

    data.code[-1], data.function_name = cammel_to_snake_case(data.code[-1])

    print("Please, choose the folder to save the problem: ")
    folder = input()
    create_folder_if_needed(folder)
    os.remove("tmp.txt")

    # create file
    data.file_name = get_file_name(data.title)
    with open(os.path.join("src", f"{folder}_problems", data.file_name), "w") as f:
        f.write("#!/usr/bin/env python\n")
        f.write('"""\n')
        f.write("Platform: LeetCode\n")
        f.write(f"Problem: {data.id}. {data.title}\n")
        f.write(f"URL: {data.url}\n")
        f.write('"""\n')
        f.write("\n")
        f.write("\n")
        for line in data.code:
            f.write(line)
        f.write("        pass\n")
        f.write("\n")
        f.write("\n")
        f.write('if __name__ == "__main__":\n')
        f.write("    solution = Solution()\n")
        for i in range(len(data.inputs)):
            f.write(
                f"    assert solution.{data.function_name}({data.inputs[i]}) == {data.outputs[i]}\n"
            )
        f.write("")

    # # create tests
    with open(os.path.join("src", f"{folder}_problems", f"test_{folder}.py"), "a") as f:
        f.write("\n")
        f.write("\n")
        f.write('"""\n')
        f.write(f"Test {data.id}. {data.title}\n")
        f.write('"""\n')
        f.write("\n")
        f.write("\n")
        f.write('@pytest.fixture(scope="session")\n')
        f.write(f"def init_variables_{data.id}():\n")
        f.write(
            f"    from src.{folder}_problems.{data.file_name[:-3]} import Solution\n"
        )
        f.write(f"    solution = Solution()\n")
        f.write("\n")
        f.write(f"    def _init_variables_{data.id}():\n")
        f.write("        return solution\n")
        f.write("\n")
        f.write(f"    yield _init_variables_{data.id}\n")
        f.write("\n")
        f.write(f"class TestClass{data.id}:")
        for i in range(len(data.inputs)):
            f.write("\n")
            f.write(f"    def test_solution_{i}(self, init_variables_{data.id}):\n")
            f.write(
                f"        assert init_variables_{data.id}().{data.function_name}({data.inputs[i]}) == {data.outputs[i]}\n"
            )

    # update readme
    with open("README.md", "r+") as f:
        for line in f:
            pass
        last_id = int(line.split()[0][1:])
        f.write(
            f"\n|{last_id + 1} |[{data.title}](src/{folder}_problems/{data.file_name})|[{folder}](src/{folder}_problems)|{data.difficulty}|[Leetcode]({data.url})|"
        )


def submit_question():
    pass


if __name__ == "__main__":
    clize.run(get_question, submit_question)
