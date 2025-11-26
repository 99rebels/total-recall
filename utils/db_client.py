
from dotenv import load_dotenv
load_dotenv()

import os
from supabase import create_client

import json

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)


# this function gets the notes from a date givin as an argument. It is called from two locations. app.py and script.py the duplication of writing the function twice. 


def get_notes(date, note_id = None, llm_questions = None):
    notes  = (
        supabase.table("notes")
        .select("*",)
        .eq("created_at", date)
        .execute()
    )

    for note in notes.data:
        print(note.values())

        questions = (
        supabase.table("questions")
        .select("question")
        .eq("main_id", int(note["id"]))
        .execute()
        )

        question_list = []

        for questions in questions.data:
            question_list.append(questions["question"])

        note.update({"question": question_list})


        
        if llm_questions is not None:
            if int(note_id) in note.values():
                note.update({"generated_questions": llm_questions})
            else:
                continue
        else:
            continue

    return notes.data