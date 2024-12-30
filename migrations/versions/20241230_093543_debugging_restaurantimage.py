"""Debugging RestaurantImage

Revision ID: 087fcde62dff
Revises: 10e75d298727
Create Date: 2024-12-30 09:35:43.099163

"""
from alembic import op
import sqlalchemy as sa

import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")


# revision identifiers, used by Alembic.
revision = '087fcde62dff'
down_revision = '10e75d298727'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    schema = os.environ.get("SCHEMA") if environment == "production" else None
    op.create_table('restaurant_images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('restaurant_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurants.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema=schema
    )

    with op.batch_alter_table('restaurants', schema=None) as batch_op:
        batch_op.alter_column('date',
                existing_type=sa.TIMESTAMP(),
                type_=sa.TIMESTAMP(),
                existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('restaurant_images')

    with op.batch_alter_table('restaurants', schema=None) as batch_op:
        batch_op.alter_column('date',
                existing_type=sa.TIMESTAMP(),
                type_=sa.TIMESTAMP(),
                existing_nullable=False)
    # ### end Alembic commands ###
