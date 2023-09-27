"""Create the database and run migrations."""
from migrations.migrator import main as migrate


def main():
    """Main function."""
    migrate()


if __name__ == "__main__":
    main()
