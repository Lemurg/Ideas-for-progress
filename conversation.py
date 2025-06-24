from states import (
    MAIN_MENU,
    SUBMIT_IDEA_TEXT,
    SUBMIT_IDEA_CONFIRMATION,
    MY_IDEAS_LIST,
    IDEA_DETAILS,
    IDEA_DETAILS_SELECT,
    MODERATION_PANEL,
    ADD_AN_MODERATION,
    MODERATION_LIST,
    MODERATION_DECISION,
    MODERATION_COMMENT,
    ANALYTICS_VIEW,
)

from handlers import (
    start_command,
    handle_role_choice,
    receive_new_ideas,
    confirm_idea_submission,
    list_of_my_ideas,
    idea_details,
    show_idea_choices,
    moderation_panel,
    add_moderation,
    moderation_list,
    moderation_decision,
    moderation_comment,
    analytics_view
)

from telegram.ext import (
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    filters
)


def create_conversation_handler():
    ConversationHandler(
        entry_points=[CommandHandler("start", start_command)],
        states={
            MAIN_MENU: [
                MessageHandler(filters.TEXT & ~filters.COMMAND,
                               handle_role_choice)
            ],

            # "Идеи"
            SUBMIT_IDEA_TEXT: [
                MessageHandler(filters.TEXT & ~filters.COMMAND,
                               receive_new_ideas),
            ],

            SUBMIT_IDEA_CONFIRMATION: [
                MessageHandler(filters.TEXT & ~filters.COMMAND,
                               confirm_idea_submission)
            ],

            # "Список идей"

            MY_IDEAS_LIST: [
                MessageHandler(filters.TEXT & ~filters.COMMAND,
                               list_of_my_ideas),
            ],
            IDEA_DETAILS: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, idea_details),
            ],
            IDEA_DETAILS_SELECT: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, idea_details)
            ],

            # "Admin"

            MODERATION_PANEL: [
                MessageHandler(filters.TEXT & ~filters.COMMAND,
                               moderation_panel),
            ],
            ADD_AN_MODERATION: [
                # здесь проверяем код доступа
                MessageHandler(filters.TEXT & ~filters.COMMAND,
                               add_moderation),
            ],
            MODERATION_LIST: [
                MessageHandler(filters.TEXT & ~filters.COMMAND,
                               moderation_list),
            ],
            MODERATION_DECISION: [
                MessageHandler(filters.TEXT & ~filters.COMMAND,
                               moderation_decision),
            ],
            MODERATION_COMMENT: [
                MessageHandler(filters.TEXT & ~filters.COMMAND,
                               moderation_comment),
            ],
            ANALYTICS_VIEW: [
                MessageHandler(filters.TEXT & ~filters.COMMAND,
                               analytics_view),
            ],
        },
        fallbacks=[CommandHandler("start", start_command)],
        allow_reentry=True,
    )