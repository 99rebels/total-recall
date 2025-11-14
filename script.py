# A script that will run at a certain time each morning, sending a email to the user of the notes/questions to revise (allows user to not have to go to Total Recall)


from datetime import datetime, timedelta
from dotenv import load_dotenv
load_dotenv()

from utils.db_client import get_notes

date = datetime.now()
day_prior = str(date - timedelta(days=1))
week_prior = str(date - timedelta(days=7))
month_prior = str(date - timedelta(days=30))
three_month_prior = str(date - timedelta(days=90))


day_prior_data = get_notes(day_prior)
week_prior_data = get_notes(week_prior)
month_prior_data = get_notes(month_prior)
three_month_prior_data = get_notes(three_month_prior)