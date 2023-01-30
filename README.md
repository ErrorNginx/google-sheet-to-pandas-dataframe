# google-sheet-to-pandas-dataframe
To convert Google Sheets data into a Pandas DataFrame, you can use the gspread library and df = pd.DataFrame(worksheet.get_all_values()).

tall the gcloud CLI.

Required roles
To get the permissions that you need to manage service account keys, ask your administrator to grant you the Service Account Key Admin (roles/iam.serviceAccountKeyAdmin) IAM role on the project, or the service account whose keys you want to manage. For more information about granting roles, see Manage access.

For more information, see Service Accounts roles.

IAM basic roles also contain permissions to manage service account keys. You should not grant basic roles in a production environment, but you can grant them in a development or test environment.


Create a service account key
To use a service account from outside of Google Cloud, such as on other platforms or on-premises, you must first establish the identity of the service account. Public/private key pairs provide a secure way of accomplishing this goal. When you create a service account key, the public portion is stored on Google Cloud, while the private portion is available only to you. For more information about public/private key pairs, see Service account keys.
