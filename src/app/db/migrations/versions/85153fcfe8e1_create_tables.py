from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic
revision = '85153fcfe8e1'
down_revision = None
branch_labels = None
depends_on = None


def create_bills_table() -> None:
	op.create_table(
		"bills",
		sa.Column("id", sa.Integer, primary_key=True),
		sa.Column("client_name", sa.Text, nullable=False, index=True),
		sa.Column("client_org", sa.Text, nullable=False, index=True),
		sa.Column("number", sa.Integer, nullable=False, index=True),
		sa.Column("sum", sa.Float, nullable=False, index=True),
		sa.Column("date", sa.Text, nullable=False, index=True),
		sa.Column("service", sa.Text, nullable=False, index=True),
	)


def upgrade() -> None:
	create_bills_table()


def downgrade() -> None:
	op.drop_table("bills")
