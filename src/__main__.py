from src.api.setup import init_app, start_app
from src.core.settings import (
    get_db_settings,
    get_documentation_settings,
)


def main() -> None:
    db_settings = get_db_settings()
    doc_settings = get_documentation_settings()

    app = init_app(db_settings, doc_settings)

    start_app(app)


if __name__ == "__main__":
    main()