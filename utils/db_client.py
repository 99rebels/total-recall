
from dotenv import load_dotenv
load_dotenv()

import os
from supabase import create_client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)


# this function gets the notes from a date givin as an argument. It is called from two locations. app.py and script.py the duplication of writing the function twice. 
def get_notes(date):
    notes = (
        supabase.table("notes")
        .select("*",)
        .eq("created_at", date)
        .execute()
    )
    return notes.data

def get_questions(main_id):
    questions = (
        supabase.table("questions")
        .select("question")
        .in_("main_id", main_id)
        .execute()
    )

    return questions.data