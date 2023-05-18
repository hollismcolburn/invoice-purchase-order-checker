import pandas as pd
import numpy as np

def new_index(df_po, df_inv):
    # set index on Vendor SKU/ID
    df_po.set_index('Vendor SKU_PO', inplace=True)
    df_inv.set_index('Mac Item #_INV', inplace=True)
    return df_po, df_inv


def match_items(df_po, df_inv):
    # match item by Vendor SKU (for now - may change with different vendors)
    df_combined = pd.concat([df_po, df_inv], axis=1)
    print("df_combined")
    print(df_combined)
    return df_combined


# def compare_qty(df_combined):
#     # compare quantities
#     # "Quantity_PO" & "Qty Shipped_INV"
#     # df_combined["Same Qty"] = df_combined["Quantity_PO"].isin(df_combined["Qty Shipped_INV"])
#     df_combined["Same QTY"] = np.where(df_combined["Quantity_PO"] == "Qty Shipped_INV")
#     # print(df_combined["Quantity_PO"].isin(df_combined["Qty Shipped_INV"]))
#     return df_combined


def compare_price(df_combined):
    # compare price/cost
    # "Cost_PO" & "Net Price_INV"
    pass


