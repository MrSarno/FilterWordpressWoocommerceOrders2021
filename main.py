#!/usr/bin/env python3


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                                                                     #
# A quick Python script to filter out orders from our website that don't contain physical items.                      #
#                                                                                                                     #
# 'Upgrades' are included, so some individual physical item entitlements may be overrepresented here. This is         #
# necessary as otherwise some would not be accounted for at all. There aren't any great alternatives, unfortunately.  #
#                                                                                                                     #
# John 'Sarno' Sweeney                                                                                                #
# Eleventh Hour Games                                                                                                 #
#                                                                                                                     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


#
# imports
#

import csv


#
# functions
#

def filter_orders():


    # Find the file containing exported order data, create new file to dump filtered data into

    with open('OrdersExportedFromWordpressWoocommerce.csv', 'r', encoding='utf8') as the_input, open(
            'FilteredOrderInformation.csv', 'w', newline='', encoding='utf8') as the_output:


        # Create objects to iterate over the lines of each file

        reader = csv.reader(the_input, skipinitialspace=True)
        writer = csv.writer(the_output, delimiter=',')


        # Skip the headers as they don't contain order information

        writer.writerow(next(reader))


        # Do the following for each line of order information in the exported data

        for row in reader:


            # Specify where the order status is "completed"; only proceed if order was successful & not refunded

            order_status = row[1]
            if order_status == "wc-completed":


                # Specify where the amount paid is to be found
                # only proceed if large enough for physical item(s), or is an upgrade

                amount_paid = row[2]
                float_paid = float(amount_paid)
                product_name = row[3]

                try:
                    if float_paid > 95:
                        writer.writerow(row)
                    elif product_name == "Custom Payments":
                        if float_paid > 20:
                            writer.writerow(row)
                    else:
                        pass
                except ValueError:
                    print(row)

    return 0


#
# run program
#

if __name__ == '__main__':
    filter_orders()
