from django.db import connections, transaction
from .models import AllProducts

def create_shards():
    # # get all distinct categories from the AllProducts table
    # categories = AllProducts.objects.order_by().values_list('SNR_Category', flat=True).distinct()
    #
    # # create a new shard for each category
    # for category in categories:
    #     shard_name = f"AllProducts_shard_{category.lower()}"
    #     with connection.cursor() as cursor:
    #         cursor.execute(f"CREATE TABLE IF NOT EXISTS `{shard_name}` LIKE `AllProducts`")

    database_alias = 'newdb'
    category = 'Electronics_shard'
    shard_name = f"AllProducts_shard_{category.lower()}"

    shard_name = "AllProducts_shard_testbesd"
    print(shard_name)
    if database_alias not in connections:
        raise ValueError(f"No database alias '{database_alias}' found in connections.")
    connection = connections[database_alias]
    print(connection)
    # with connection.cursor() as cursor:
    with connections['newdb'].cursor() as cursor:
        # cursor.execute(f"CREATE TABLE IF NOT EXISTS {shard_name} (LIKE \"AllProducts\")")
        # cursor.execute(f"CREATE TABLE IF NOT EXISTS {shard_name} (LIKE \"AllProducts\")")
        # cursor.execute(f"CREATE TABLE IF NOT EXISTS {shard_name} (LIKE newdb.\"AllProducts\")")
        # cursor.execute(f"CREATE TABLE IF NOT EXISTS {shard_name} (LIKE newdb.public.\"AllProducts\")")
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {shard_name} (id SERIAL PRIMARY KEY, name VARCHAR(255))")


    print('Shard Created')


def insert_records():
    # get all records from the AllProducts table in chunks
    all_products = AllProducts.objects.all().order_by('SNR_Category', '-SNR_Date')
    chunk_size = 5000
    start_index = 0
    end_index = start_index + chunk_size
    while start_index < all_products.count():
        chunk = all_products[start_index:end_index]
        with transaction.atomic():
            # insert each record into the appropriate shard
            for product in chunk:
                shard_name = f"AllProducts_shard_{product.SNR_Category.lower()}"
                product_copy = AllProducts.objects.get(pk=product.pk)
                product_copy.pk = None  # create a new record instead of updating the existing one
                product_copy.save(using='newdb', table=shard_name)
        start_index = end_index
        end_index = start_index + chunk_size
