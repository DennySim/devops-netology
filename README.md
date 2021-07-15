Согласно Terraform/.gitignore будут проигнорированы:
**/.terraform/*  	 - рекурсивно все каталоги и файлы в каталоге .terraform, который может встречаться, где 
						угодно в структуре каталогов
*.tfstate            - все файлы расширением tfstate
*.tfstate.*          - все файлы, содержашие в своем названии шаблон .tfstate.
crash.log            - файл crash.log
*.tfvars             - все файлы расширением tfvars
override.tf          - файл override.tf
override.tf.json     - файл override.tf.json
*_override.tf        - все файлы с названием, оканчивающимся на _override.tf
*_override.tf.json   - все файлы с названием, оканчивающимся на _override.tf.json
.terraformrc         - файл .terraformrc
terraform.rc         - файл terraform.rc