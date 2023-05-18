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


def compare_qty(df_combined):
    # compare quantities
    df_combined = df_combined.fillna(0.0)
    df_combined["Same QTY"] = df_combined["Qty Shipped_INV"] - df_combined["Quantity_PO"]
    return df_combined


def compare_price(df_combined):
    # compare price/cost
    # "Cost_PO" & "Net Price_INV"
    df_combined = df_combined.fillna(0.0)
    df_combined["Same PRICE"] = df_combined["Net Price_INV"] - df_combined["Cost_PO"]
    return df_combined


def separate_problems(df_combined):
    # write file with only items that have differing quantities
    df_quantity = df_combined.drop(df_combined[df_combined['Same QTY'] == 0.0].index)
    
    print("df_quantity")
    print(df_quantity)

    df_quantity.to_csv("quantity.csv")

    # write file with only items that have different prices
    df_price = df_combined.drop(df_combined[df_combined['Same PRICE'] == 0.0].index)

    print("df_price")
    print(df_price)

    df_price.to_csv("price.csv")