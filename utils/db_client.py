
from dotenv import load_dotenv
load_dotenv()

import os
from supabase import create_client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)


def get_notes(date):
    get_note = (
        supabase.table("main-table")
        .select("subject", "topic", "notes", "questions")
        .eq("created_at", date)
        .execute()
    )
    return get_note.data

