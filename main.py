import files, compare

if __name__ == "__main__":

    # TODO: using Mac order for testing, update to generic file name when finished
    df_purchase_order, df_invoice = files.read_files('mac_po.csv', 'mac_invoice.csv')

    print("purchase order columns")
    print(df_purchase_order.columns)

    print("invoice columns")
    print(df_invoice.columns)

    files.drop_info_rows(df_purchase_order)
    df_po, df_inv = files.rename_columns(df_purchase_order, df_invoice)

    print("purchase order columns")
    print(df_po.columns)

    print("invoice columns")
    print(df_inv.columns)

    df_po, df_inv = compare.new_index(df_po, df_inv)

    print("purchase order")
    print(df_po.tail)

    print("invoice")
    print(df_inv.tail)

    df_combined = compare.match_items(df_po, df_inv)

    df_combined = compare.compare_qty(df_combined)
    df_combined = compare.compare_price(df_combined)

    print("combined columns")
    print(df_combined.columns)

    compare.separate_problems(df_combined)

    files.combined_file(df_combined)
