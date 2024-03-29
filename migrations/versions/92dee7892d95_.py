"""empty message

Revision ID: 92dee7892d95
Revises: 9b3c870b6cde
Create Date: 2023-12-26 09:35:37.847144

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92dee7892d95'
down_revision = '9b3c870b6cde'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=2),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.Float(precision=2),
               type_=sa.REAL(),
               existing_nullable=False)

    # ### end Alembic commands ###
