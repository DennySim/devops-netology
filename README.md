## Описание

1. Согласно Terraform/.gitignore будут проигнорированы:
**/.terraform/*  	    - рекурсивно все каталоги и файлы в каталоге .terraform, который может встречаться, где 
						угодно в структуре каталогов
2. *.tfstate            - все файлы расширением tfstate
3. *.tfstate.*          - все файлы, содержашие в своем названии шаблон .tfstate.
4. crash.log            - файл crash.log
5. *.tfvars             - все файлы расширением tfvars
6. override.tf          - файл override.tf
7. override.tf.json     - файл override.tf.json
8. *_override.tf        - все файлы с названием, оканчивающимся на _override.tf
9. *_override.tf.json   - все файлы с названием, оканчивающимся на _override.tf.json
10. .terraformrc        - файл .terraformrc
11. terraform.rc        - файл terraform.rc