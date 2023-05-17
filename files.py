import pandas as pd

def rename_columns(df_purchase_order, df_invoice):
    # add PO to end of each column name
    df_po = df_purchase_order.add_suffix('_PO')

    # add INV to end of each column name
    df_inv = df_invoice.add_suffix('_INV')

    return df_po, df_inv


def drop_info_rows(df_purchase_order):
    # drop informational rows in purchase order
    df_purchase_order.drop([156, 157, 158, 159, 160, 161, 162, 163], inplace=True)
    print(df_purchase_order.tail)

    return df_purchase_order

    # do columns need to be dropped?


def read_files(purchase_order, invoice):
    # read & clean main inventory sheet
    df_purchase_order = pd.read_csv(purchase_order, header = 0)
    # df_original = clean_main(df_original)

    df_invoice = pd.read_csv(invoice, header = 0)

    return df_purchase_order, df_invoice