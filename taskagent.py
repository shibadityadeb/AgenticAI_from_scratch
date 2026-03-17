#load env
#read task from file
#make a call to llm to categorise our task
import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

api_key =  os.getenv("CLAUDE_API_KEY")
if not api_key:
    raise RuntimeError(
        "Missing API key"
    )
client = Anthropic(api_key=api_key)
def read_task(file_path):
    with open(file_path,"r") as f:
        return f.read()


def _extract_text_from_response(message) -> str:
    blocks = getattr(message, "content", []) or []
    parts: list[str] = []
    for block in blocks:
        if getattr(block, "type", None) == "text":
            parts.append(getattr(block, "text", ""))
    return "".join(parts).strip()


def summarize_task(task):
    prompt=f"""Give me the high priority task from the list in a way it goes from the highest priority the first and then decreasing in priority: {task}"""
    response=client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1000,
        messages=[
            {"role":"user","content":prompt}
        ]
    )
    return _extract_text_from_response(response)


if __name__=="__main__":
    task_list=read_task("task.txt")
    summary=summarize_task(task_list)
    print("-"*30)
    print(summary)