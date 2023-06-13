import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random as rnd
from streamlit_extras.let_it_rain import rain

credentials = {
    "type": "service_account",
    "project_id": "corpify",
    "private_key_id": "3ac4310ae089faf9fda4f3fbc069fcd949fd4a88",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC5B7y+eQqQ16ki\nCYwFRlHIW3PX2t4GgMcz4qDD0ySIK9hHNDpQHsu2yG9n0ERmJ740GXTB3it6rSAA\n7BAflhR6EZ5Mm8TkaPBY7FlH5fh3gI6fdRYN1+hf0SkHRj4L5LRiRNbS9dC9OMJd\nzUpk0BK/8UmqLiq2djL6l05ny/+HKsGG/OKqs5uUjm3vPfHs/+tQfT6uf5kPrUbi\noFFjZHU6Yr4g/5Jw12uvyputJ2tXP+KSOF3fiEFSD2mvftTD3dVS/gUNkzPntQJL\nC35iGWRSmJ3AOBWWvYP9UDVRutyVjUDreY45aizJByMU+KXDW613DwG4DKnqxKjP\noysoHj+tAgMBAAECggEADphikM1y938aJ2YZ465K6V30usLtZGrC69/qqa/C0AlS\nBOHaNLONLa9MrGN0YHDY8yVL6Av/9ta9BshC3amkwVvuQPbrlnnZoFC6b9kJ2wFV\ndBS+vIZQB+4ziTrxo4Cy+D/GXfsyb+6lfv6LKahzxizAuw9rt/Cwb5hrq0qJ7u3e\nYGoJK5z64zX9v3kf7teYwDJgGv4XAvbPN7iTkWuwKvpqWCBsxGl9w1SPowqz1P2p\nFvN9p62Ev+jFuhK6J5vuWxB4kA0i7yynwMmcmn6hws6nX0xyFid2eDUH4qRYOE4q\nb8+FB5jAQnCupNfB69qqw+41awMt7vNwNKdN4nuwkQKBgQDwyyz1HHuCmSwL8b9G\ncKPYWRqynUEx2tEbtdBKW9jLb9YbMrYtmcNVieg/Sl9hozDBFmQPBcZeA2SKZGuL\nSyF7FMvN8I62naEO0m9ulZ2YJgpS0fZiTeOwJzAZmWrPZn03BWCnTL0QpMdzIvpH\nftwBQwiskhtTEfpOdPqeHOGG/QKBgQDEtw3pNPWYgh1h2Pi2p36fU2M98WrOZ4Yw\nJGAdDLlpX5bgFiIYsJ8NhQabemG360ZWhMjPVM6bGx+1fkggW22DezfRMv6nq/V5\njf4dCktHlgruTQsr8LbmtSpZrZBKW+FTJRO5Alott0xn3wYgMCypiWMJya1d6/tZ\ni307JtlycQKBgQDbAYBfY0t2ygfEyViWIab0BH8Cy4JbbNDZ6jCLISR6S7qpvCL0\nMLD34NlqjyNXc4zJYasZ+r+kDGPqd1FVPL0z7AM9yLiUoaO2DnGpW80dcCPdlfgJ\nCxy2v73A2sfJ4Uarv2lcYLBpLeX18289jcVeJHEEPFM759MIft7e5he9pQKBgQC4\nrb6SnVShHC6niQJewLrgq3G1WqvSIWDaW5wcSbDcG5DSyhSyp0Z7c9LzLp8FAw3i\n9gBsnYrmFT3crzTZo9wZnxmU/lITah4oQ0U5UEvCZjvW41/EndWonJao4IhhNwdA\nfsOYYnv1BWvm7Hucxn13oPLo4n0vevdbZthoKx3kEQKBgGzTWzC8OMYFbIVNKkki\nfJSXtawb34UQY3BPM1eih9OpWzAm7/EumouF7vTrVbfLQPgrwKQkr9jkNQ7bF5du\nO8zOUYU6s54Zo113nHj2eW7kJEx6EixDw5W54lwxRIIjIkAlAv8HQjni1TDRwHVL\n9qbWdI6YW2i3NiqgVGDEtrvx\n-----END PRIVATE KEY-----\n",
    "client_email": "corpify@corpify.iam.gserviceaccount.com",
    "client_id": "116968765567863905682",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/corpify%40corpify.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}


def writing_task_collect_data():
    """
    Explains the writing task (of providing a new source sentence),
    and collects the sentence the user contributed.
    :return: None
    """
    st.write("### Contribute a sentence that needs to be corpified")
    st.write("##### What is your task")
    st.write("Your task is to come up with a sentence (in English) that you would like to "
             "'corpify' (meaning - rephrased in a corporate-friendly manner).\n"
             "This should be something you would think to yourself or want to say to a colleague, manager or employee, "
             "***but you can't say it like that because it would be unproffesional.***")
    st.write("Check out the examples in ❔ down here on the right!")

    # Get sentence from user
    st.text_input("Please enter a sentence in spoken English that you would like us to corpify:", key="task1_output",
                  help="Examples: 'I know you saw my message, stop ignoring me!' or 'Well that's a dumb idea'.\n"
                       " You don't need the quoation marks, just write you sentence as it is.")
    st.button("Contribute", on_click=move_page_to_after_task1)


def rephrasing_task_collect_data():
    """
     Explains the rephrasing task (of providing a new target sentence for an existing source sentence),
     Chooses a random source sentence that doesn't have a target sentence yet,
     And collects the user's rephrasing for that sentence.
    :return: None
    """
    st.write("### Contribute by rephrasing a sentence to a corpy style")
    st.write("##### What is your task")
    st.write("You will be provided with a normal English sentence. "
             "Your task is to **re-write the sentence to match a corporate & professional setting.** "
             "You don't need to rephrase it word-by-word - you have creative freedom as for how to "
             "catch the essence of the original sentence while making it corpy.\n"
             "Don't be afraid to be passive-aggressive or fake-nice if necessary, as these micro-aggressions is the fuel of corpy culture... 🙄")

    source_sentences = state.sheet.col_values(1)  # read the A column from Google Sheets
    target_sentences = state.sheet.col_values(2)  # read the B column from Google Sheets

    source_last_row_ind = len(source_sentences)
    target_last_row_ind = len(target_sentences)

    sents_to_translate = []
    for row in range(1, source_last_row_ind):
        if (row < target_last_row_ind and target_sentences[row] == "") or (row >= target_last_row_ind):
            source_sent = source_sentences[row]
            sents_to_translate.append((source_sent, row))

    if len(sents_to_translate) > 0:  # there are available sentences to rephrase
        state.chosen_sent, state.chosen_row = rnd.choice(sents_to_translate)  # choose random non translated sentence
        st.write("##### What to re-write\nPlease re-write the following sentence:")
        st.write(f"##### ***{state.chosen_sent}***")
        st.write("Check out the examples in ❔ down here on the right!")
        st.text_input("Re-write the bolded sentence in a corporate manner:",
                      key="task2_output", help="Examples: 'Don't interrupt me' could be rephrased as "
                                               "'Thank you for you input, but please wait until I am "
                                               "finished sharing my thoughts before proceeding', and "
                                               "'I hate your idea' could be rephrased as 'Let’s circle back on this'.")
        st.button("Contribute", on_click=move_page_to_after_task2)
    else:  # there are no available sentences to rephrase
        st.write("##### Oh no! We currently don't have any sentences for you to corpify 😔\n"
                 "If you want to help us with that, you can propose sentences of your own! "
                 "Just refresh this page and click 'Add a sentence'.")
        st.write("**You can always come back later and hopefully we will collect more sentences by then!**")


def writing_task_save_to_sheets():
    """
    Called after a new source sentence from the user was collected via writing_task_collect_data.
    Writes the collected sentence into the Google Sheets database.
    :return: None
    """
    next_row_ind = len(state.sheet.col_values(1)) + 1  # choose index to write to
    state.sheet.update('A' + str(next_row_ind), state.task1_output)  # Write sentence to Sheets
    state.cur_page = "thanks"


def rephrasing_task_save_to_sheets():
    """
    Called after a new target sentence from the user was collected via rephrasing_task_collect_data.
    Writes the collected sentence into the Google Sheets database.
    :return: None
    """
    try: # ignore wierd unexplained exception that doesn't impact functionality
        state.sheet.update('B' + str(state.chosen_row + 1), state.task2_output)  # Write sentence to Sheets
    except KeyError or AttributeError:
        pass
    state.cur_page = "thanks"


def move_page_to_task1():
    """
    Changes the page to show instructions for the writing task.
    :return: None
    """
    state.cur_page = "task1"


def move_page_to_task2():
    """
    Changes the page to show instructions for the rephrasing task.
    :return: None
    """
    state.cur_page = "task2"


def move_page_to_after_task1():
    """
    Changes the page to save the collected data of the writing task.
    :return: None
    """
    state.cur_page = "after_task1"


def move_page_to_after_task2():
    """
    Changes the page to save the collected data of the rephrasing task.
    :return: None
    """
    state.cur_page = "after_task2"


def thanks_for_contributing():
    """
    Shows a thank-you message along with raining lots of thank-you emojis.
    :return: None
    """
    rain(
        emoji="🙏👩‍💼",
        font_size=40,
        falling_speed=5,
        animation_length="infinite",
    )
    st.write("# Thanks for contributing to the Corpify project!")
    st.write("#### Every contribution is meaningful!\n**If you want to contribute some more - choose a task:**")
    st.button('Add a sentence you want us to corpify', on_click=move_page_to_task1)
    st.button('Rephrase a sentence to a corpy style', on_click=move_page_to_task2)
    st.write("If youv'e had enaugh you can just close this tab")


state = st.session_state  # initialize state to save info to

# when app first opens:
if "sheet" not in state:
    state.cur_page = "main"

    # connect to google sheets
    gc = gspread.service_account_from_dict(credentials)
    sh = gc.open("Corpify_data_collection")
    state.sheet = sh.worksheet("Sheet1")

    # show general instructions
    st.write("## Contribute Data to the Corpify Project 🧑‍💼")
    st.write("##### What is the Corpify project?")
    st.write(
        "Corpify is an open-source academic NLP project that aims to develop a model that rephrases text in everyday English into the beloved dialect of corporate-English. "
        "The goal is to help frustrated corporate employees to communicate their thoughts and feelings in the "
        "familiar corporate manner we all know and love *so much* (or just amuse them on their coffee break).")
    st.write("##### Who can contribute")
    st.write("If you speak English and are familiar with the vibes of workplace communication in the American corporate world, we want your input!")
    st.write("##### How can I help?")
    st.write(
        "You can propose a sentence of your own that needs to be corpified, or help us by re-writing sentences that others suggested into a corpy language. Both are super fun! 🔥")
    st.write("Your contribution will be donated (anonymously and without pay) to a dataset that will be used to train our "
             "open-source Corpify rephrasing model.\n"
             "Both the dataset and the trained model will be made publicly available via HuggingFace.")
    st.write("**Choose your way to contribute**")
    st.button('Add a sentence you want us to corpify', on_click=move_page_to_task1)
    st.button('Rephrase a sentence to a corpy style', on_click=move_page_to_task2)

# Flow control for every stage after the main page:

if state.cur_page == "task1":
    writing_task_collect_data()

if state.cur_page == "task2":
    rephrasing_task_collect_data()

if state.cur_page == "after_task1":
    writing_task_save_to_sheets()

if state.cur_page == "after_task2":
    rephrasing_task_save_to_sheets()

if state.cur_page == "thanks":
    thanks_for_contributing()
