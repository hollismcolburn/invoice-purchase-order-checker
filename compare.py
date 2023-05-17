import pandas as pd

def new_index(df_po, df_inv):
    # set index on Vendor SKU/ID
    df_po.set_index('Vendor SKU_PO', inplace=True)
    df_inv.set_index('Mac Item #_INV', inplace=True)
    return df_po, df_inv



    # match item by Vendor SKU (for now - may change with different vendors)
    