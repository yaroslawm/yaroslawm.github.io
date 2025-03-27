import json, boto3, os
from botocore.exceptions import ClientError
###########################################################

def lambda_handler(event, context):
    s3_client = boto3.client('s3')
    bucket_name = 'bkp-cv-20240205155006346900000001'
    prefix = 'maintenance_page/'
    files = ['index.html', 'style.css', 'Group.png']
    tmp_dir = '/tmp/'
    # lambda_root = os.environ.get('LAMBDA_TASK_ROOT', '.')
    
    # Витягуємо файли з S3 bucket
    for file in files:
        try:
            s3_client.download_file(bucket_name, prefix+file, os.path.join(tmp_dir, file))
            print(f"Завантажено файл: {file}")
        except ClientError as e:
            print(f"Помилка завантаження файлу {file}: {e}")

    # obj = s3.get_object(Bucket=bucket_name, Key=f'{folder_name}/{file_name}')
    # index_file = s3_client.get_object(Bucket=bucket_name, Key=f'{folder_name}/{file1_name}')['Body'].read().decode('utf-8')
    # style_file = s3_client.get_object(Bucket=bucket_name, Key=f'{folder_name}/{file2_name}')['Body'].read().decode('utf-8')
    # image_file = s3_client.get_object(Bucket=bucket_name, Key=f'{folder_name}/{file3_name}')['Body'].read()


    # image_base64 = base64.b64encode(image_file).decode('utf-8')
    # html_content = obj['Body'].read().decode('utf-8')
    # Формуємо статичну сторінку
    m_page = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Document</title>
<link rel="stylesheet" href="/tmp/style.css">
</head>
<body>
<section class="container">
<h1 class="title">Вибачте, наш сайт оновлюється2 :(</h1>
<img src="/tmp/Group.png">
</section>
</body>
</html>
    """
    with open(os.path.join(tmp_dir, 'index.html'), 'r') as f:
        maintenance_page = f.read()
    # print(s3://bkp-cv-20240205155006346900000001/maintenance_page/index.html)
    
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html; charset=utf-8',
        },
        'body': m_page
    }    
    
    
    
    # try:
    #     # obj = s3.get_object(Bucket=bucket_name, Key=file_name)
    #     obj = s3.get_object(Bucket=bucket_name, Key=f'{folder_name}/{file_name}')      
    #     html_content = obj['Body'].read().decode('utf-8')
    #     img_obj = s3.get_object(Bucket=bucket_name, Key=f'{folder_name}/Group.png')
    #     img_content_bytes = img_obj['Body']
    #     # img_content = base64.b64encode(img_content_bytes).decode('utf-8')        
    #     # img_content = img_obj['Body'].read().decode('base64')

    #     # img_content = b64encode(img_content_bytes).decode('utf-8')        
    #     # html_with_img = html_content.replace('<!-- IMAGE\_PLACEHOLDER -->', f'<img src="data:image/png;base64,{img\_content}"/>')
    #     # html_with_img = html_content.replace('<!-- IMAGE_PLACEHOLDER -->', f'<img src="data:image/png;base64,{img_content}"/>')
    #     # html_with_img = html_content.replace('<img src="Group.png">', f'<img src="{img_obj}">')
    #     html_with_img = html_content.replace('<img src="Group.png">', f'<img src="{img_content_bytes}">')
    # except Exception as e:
    #     print(f"<h1><font color=red>error: {str(e)}</font></h1><br><br>")
    #     response = {
    #         "statusCode": 500,
    #         "headers": {"Content-Type": "text/html; charset=utf-8"},
    #         "body": f"<h2>Error occurred: {str(e)}</h2>"
    #     }
    #     return response

    # response = {
    #     "statusCode": 200,
    #     "headers": {"Content-Type": "text/html; charset=utf-8"},
    #     "body": html_with_img
    # }
    # return response







############################################################
# def lambda_handler(event, context):
#     buckets = boto3.client('s3')
#     website_configuration = {
#         'IndexDocument': {'Suffix': 'index.html'},
#     }
#     try:
#         results = buckets.list_buckets()
#         print(results)
#         output = ""
#         for bucket in results['Buckets']:
#             output = output + bucket['Name'] + "\n"
#         print("<h1><font color=green>bucket name:</font></h1><br><br>" + output)
#     except:
#         print("<h1><font color=red>error</font></h1><br><br>")
#     # result = s3.get_bucket_website(Bucket='bkp-cv-20240205155006346900000001')
#     # s3://bkp-cv-20240205155006346900000001/maintenance_page/index.html
#     # rslt = buckets.get_bucket_website(Bucket='bkp-cv-20240205155006346900000001')
#     response = {
#         "statusCode": 200,
#         "headers"   : {"Content-Type": "text/html; charset=utf-8"}, 
#         "body"      : "<h2>Normal Page bucket:"+output+"</h2>"
#         #"body"      : "<h2>Normal Page bucket:"+output+"</h2>"
#     }
#     return response
