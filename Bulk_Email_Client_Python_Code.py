import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


bcc_id = ['  Testing@Stockyana.com ' ]
rec =  ', '.join(bcc_id)
bcc_id_9 = 'Testing2@Stockyana.com'
bcc_id_10 = 'Testing3@Stockyana.com'
bcc_id_11 = 'Testing4@Stockyana.com'
bcc_id_12 = 'Testing5@Stockyana.com'
bcc_id_13 = 'Testing6@Stockyana.com'
bcc_id_14 = 'Testing7@Stockyana.com'
bcc_id_15 = 'Testing8@Stockyana.com'
bcc_id_16 = 'Testing9@Stockyana.com'
bcc_id_17 = 'Testing10@Stockyana.com'
bcc_id_18 = 'Testing11@Stockyana.com'
bcc_id_19 = 'Testing12@Stockyana.com'
bcc_id_20 = 'Testing13@Stockyana.com'
bcc_id_21 = 'Testing14@Stockyana.com'
bcc_id_22 = 'Testing15@Stockyana.com'








sender_email = 'Sachin.sharma@stockyana.com'
sender_password = 'ABCFD'
smtp_server = 'smtp.gmail.com'
smtp_port = 587

csv_file = 'C:/Users/Stockyana/Desktop/Clients.csv'
df = pd.read_csv(csv_file)

for Client_name, Customer_rows in df.groupby('customer'):
    Client_email = Customer_rows.iloc[0]['Email ID']
    toaddrs = [Client_email] + [rec] +  [bcc_id_9]  + [bcc_id_10]  + [bcc_id_11]  + [bcc_id_12]  + [bcc_id_13] + [bcc_id_14]  + [bcc_id_15]  + [bcc_id_16]  + [bcc_id_17] + [bcc_id_18]   + [bcc_id_19] + [bcc_id_20] + [bcc_id_21] + [bcc_id_22]    

    message = MIMEMultipart()
    message['From'] = ' Analytics_Team_ <{}>'.format(sender_email)
    message['To'] = ', '.join(toaddrs)
    #zmessage['CC'] = '  sachin@stockyana,com    ', 'info@stockyana.com'
    message['Subject'] = '<IMP> New Product launch Alert - {}'.format(Client_name)

    body = """
    <html>
        <head>
            <style>
                table {{
                    border-collapse: collapse;
                    width: 100%;
                }}
                th, td {{
                    text-align: left;
                    padding: 8px;
                    border: 1px solid black;
                }}
                th {{
                    background-color: #f2f2f2;
                }}
                tr:nth-child(even) {{
                    background-color: #f9f9f9;
                }}
            </style>
        </head>
        <body>
            <p>Hi,</p>
            <p>Important Alert for our Valuable Customer </p>
            <p>We have introduce a new product in the Market that will make your work more easy </p>
            <table>
                <tr>
                    <th>Name</th>
                    <th>Customer_Mobile</th>
                    <th>Email_id</th>
                    <th>Vehicle_Type</th>
                    <th>Address</th>
                    <th>City</th>
                    <th>State</th>
                    <th>Update</th>
                    <th>Unique_ID</th>
                </tr>
    """

    for row in Customer_rows.itertuples(index=False):
        body += """
                <tr>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                </tr>
        """.format(row.Name, row.Customer_Mobile, row.Email_id, row.Address, row.City, row.State, row.Update, row.Unique_ID, row.CUST_ID)

    body += """
            </table>
            <p>Warm Regards,</p>
            <p>Sachin Sharma (+919034283082)</p>
            <p>Stockyana.com</p>
        </body>
    </html>
    """

    # Attach HTML content to the email
    message.attach(MIMEText(body, 'html'))

    # Send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, toaddrs, message.as_string())
        server.quit()
        print("Email sent to {} at {}".format(Client_name, Client_email))
    except Exception as e:
        print("Error sending email to {}: {}".format(Client_name, str(e)))
