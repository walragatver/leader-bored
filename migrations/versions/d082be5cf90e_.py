"""empty message

Revision ID: d082be5cf90e
Revises: f7d944091190
Create Date: 2020-05-31 16:07:07.202017

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd082be5cf90e'
down_revision = 'f7d944091190'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('contest_name', sa.String(), nullable=False),
    sa.Column('starting_at', sa.DateTime(), nullable=True),
    sa.Column('durationSeconds', sa.Integer(), nullable=False),
    sa.Column('contest_type', sa.Enum('CF', 'IOI', 'ICPC', name='contest_types'), server_default='CF', nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('is_added', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_contests'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contests')
    # ### end Alembic commands ###
