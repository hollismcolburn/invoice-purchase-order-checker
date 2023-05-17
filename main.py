import files, compare

if __name__ == "__main__":

    # TODO: using Mac order for testing, update to generic file name when finished
    df_purchase_order, df_invoice = files.read_files('mac_po.csv', 'mac_invoice.csv')

    print("purchase order columns")
    print(df_purchase_order.columns)

    print("invoice columns")
    print(df_invoice.columns)
