from datetime import datetime, timedelta
from glob import glob
import random
import os


JOURNAL_PATH = os.path.dirname(__file__)
ENTRY_PATH = JOURNAL_PATH + "/" + "entries"
WEEKLY_PROMPT_PATH = JOURNAL_PATH + "/" + "weekly_prompts"


def is_first_entry_this_week():
    """ 
    checks the entries dir to determine if this is the first entry for the week.
    """
    cur_date = datetime.now()
    cur_day = cur_date.today().weekday()
    for i in range(0, cur_day + 1):
        entry_date = cur_date.today() - timedelta(days=(cur_day - i))
        files = glob(ENTRY_PATH + "/" + entry_date.strftime("%Y%m%d-") + "*.txt")
        if files: return False
    return True


def grab_daily_writing_prompt():
    """ 
    gets a daily prompt from the prompt file. maybe a db in the future.
    """
    writing_prompts = [line.rstrip("\n") for line in open("daily_prompts.txt")]
    return random.choice(writing_prompts)


def grab_weekly_writing_prompt():
    """ 
    gets a weekly prompt from the prompt file. maybe a db in the future.
    """
    files = os.listdir(WEEKLY_PROMPT_PATH)
    chosen_prompt = random.choice(files)
    with open(WEEKLY_PROMPT_PATH + "/" + chosen_prompt, "r") as file:
        content = file.read()
    return content


def get_entry_name():
    """
    gets the date-time name for the journal entry
    """
    cur_date = datetime.now()
    return cur_date.strftime("%Y%m%d-%H%M")


def create_entry():
    """
    create a journal entry with some text pulled from writing prompts and date info 
    """
    is_first_entry = is_first_entry_this_week()
    
    entry_file = open(ENTRY_PATH + "/" + get_entry_name() + ".txt", "w+")
    entry_file.write(get_entry_name() + "\r\n")

    if (is_first_entry):
        entry_file.write("\r\n=== WEEKLY PROMPT ===\r\n")
        entry_file.write(grab_weekly_writing_prompt())
        entry_file.write("\r\n=====================\r\n")
    
    entry_file.write("\r\n--- DAILY PROMPT ---\r\n")
    entry_file.write(grab_daily_writing_prompt())
    entry_file.write("\r\n--------------------\r\n\r\n")


def main():
    create_entry()


if __name__ == "__main__":
    main()