Para executar, acessar o arquivo manage.py e digitar
	python manage.py runserver


A base de dados se encontra dentro do projeto onde existe um usuario (id=3) vitor

Para executar testes simples, o arquivo test.py que executa comandos de testes post e get apenas
mudando a URL, a autorização foi desenvolvido com Token simples e o arquivo de manage pode ser usado
para criar um novo usuario (manage.py createsuperuser) e gerar token para esse usuario

A area de admin(http://127.0.0.1:8000/admin/) pode ser usada para verificar o banco de dados e incluir 
novos itens (usuarios/tokens/livros). Para acessar utilize o arquivo manage.py e crie um novo superusuario