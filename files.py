import pandas as pd

def read_files(purchase_order, invoice):
    # read & clean main inventory sheet
    df_purchase_order = pd.read_csv(purchase_order, header = 0)
    # df_original = clean_main(df_original)

    df_invoice = pd.read_csv(invoice, header = 0)

    return df_purchase_order, df_invoice