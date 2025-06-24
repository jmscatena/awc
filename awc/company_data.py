"""
This module provides data for the company website.
In a real application, this would likely come from a database.
"""
from django import forms
from django.forms import TextInput


class ContactForm(forms.Form):
    """Form for website visitors to contact the company"""
    name = forms.CharField(
        label='Nome',
        min_length=2,
        max_length=100,
        widget=TextInput(attrs={
            'class': 'form-control form-control-lg',
            'id': 'name-input',
            'placeholder': 'Digite seu nome'
        }),
        error_messages={
            'required': 'Nome Obrigatório',
            'min_length': 'Nome precisa ter entre 2 a 100 caracteres',
            'max_length': 'Nome precisa ter entre 2 a 100 caracteres',
        }
    )

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control form-control-lg',
            'id': 'email-input',
            'placeholder': 'Entre com seu email'
        }),
        error_messages={
            'required': 'Email obrigatório',
            'invalid': 'Entre com um email válido'
        }
    )

    subject = forms.CharField(
        label='Assunto',
        min_length=3,
        max_length=200,
        widget=TextInput(attrs={
            'class': 'form-control form-control-lg',
            'id': 'subject-input',
            'placeholder': 'Digite a mensagem'
        }),
        error_messages={
            'required': 'Assunto obrigatório',
            'min_length': 'Assunto deve conter entre 3 a 200 caracteres',
            'max_length': 'Assunto deve conter entre 3 a 200 caracteres',
        }
    )

    inquiry_type = forms.ChoiceField(
        label='Categoria',
        choices=[
            ('', 'Selecione a categoria'),
            ('project', 'Projetos - Informações'),
            ('course', 'Cursos - Informações'),
            ('training', 'Programa de Treinamento'),
            ('publication', 'Publicações'),
            ('partnership', 'Parcerias'),
            ('other', 'Outros')
        ],
        widget=forms.Select(attrs={
            'class': 'form-select form-select-lg',
            'id': 'inquiry-type-input'
        }),
        error_messages={
            'required': 'Please select an inquiry type'
        }
    )

    message = forms.CharField(
        label='Mensagem',
        widget=forms.Textarea(attrs={
            'class': 'form-control form-control-lg',
            'id': 'message-input',
            'rows': 5,
            'placeholder': 'Digite sua mensagem'
        }),
        min_length=10,
        max_length=2000,
        error_messages={
            'required': 'Mensagem obrigatória',
            'min_length': 'Mensagem deve conter entre 10 a 2000 caracteres',
            'max_length': 'Mensagem deve conter entre 10 a 2000 caracteres',
        }
    )


def get_company_info():
    """Return company information for the website"""
    return {
        'name': 'AllWorks Company',
        'short_name': 'AWC',
        'slogan': 'Entregando Excelência em Projetos, Cursos e Treinamentos',
        'founded': 2020,
        'mission': 'Fornecer soluções inovadoras e experiências de aprendizagem excepcionais que capacitem organizações e indivíduos a atingir seu potencial máximo.',
        'vision': 'Ser o principal fornecedor de serviços profissionais, educação e soluções de treinamento globalmente, reconhecido pela excelência e inovação.',
        'core_values': [
            'Excelência em tudo o que fazemos',
            'Inovação e criatividade<br><br>',
            'Integridade e prática ética<br><br>',
            'Abordagem centrada no cliente',
        ],
        'headquarters': 'Ribeirão Preto, SP',
        'team_size': '',
        'certifications': [
            'Profissionais Mestres e Doutores',
            'CISCO Instructor',
            'CyberOPS Associate',
            'CCNA I V.7',
        ]
    }

def get_projects():
    """Return list of company projects"""
    return [
        {
            'id': 1,
            'title': 'SGDoc - Sistema de Gestão de Documentos',
            'category': 'Desenvolvimento',
            'client': 'Faculdade de Tecnologia - Fatec',
            'description': '  A solução definitiva para otimizar o fluxo de informações e a organização documental na sua faculdade. Desenvolvido para atender às necessidades específicas de instituições de ensino, o SGDI centraliza e gerencia com eficiência todos os documentos internos, desde atas de reunião e regulamentos acadêmicos até históricos de alunos e contratos de funcionários.',
            'image': 'images/sigdoc.jpg',
            'highlights': [
                '<strong>Centralização</strong>: Tudo em um só lugar.',
                '<strong>Segurança</strong>: Proteção e controle de acesso.',
                '<strong>Eficiência</strong>: Agilidade nos processos.',
                '<strong>Organização</strong>: Estrutura e fácil localização.',
                '<strong>Conformidade</strong>: Auditoria e rastreabilidade.',

            ],
            'duration': '06 months',
            'year': 2025
        },
        {
            'id': 2,
            'title': 'Reconhecimento Facial Múltiplo',
            'category': 'Pesquisa',
            'client': 'Faculdade de Tecnologia - Fatec',
            'description': 'Projetado e implementado para soluções de cidade inteligente para mobilidade urbana, monitoramento ambiental e segurança pública, '+
                           'explorando metodologias e tecnologias para identificar e analisar simultaneamente diversas faces em ambientes complexos. '+
                           'Esta área se dedica aos desafios e oportunidades que surgem da presença de múltiplas pessoas em uma cena, seja em imagens estáticas ou fluxos de vídeo.',
            'image': 'images/facerec.jpg',
            'highlights': [
                '<strong>Simultaneidade</strong>: Múltiplas faces ao mesmo tempo.',
                '<strong>Complexidade</strong>: Cenários desafiadores e dinâmicos.',
                '<strong>Rastreamento</strong>: Acompanhamento contínuo.',
                '<strong>Análise</strong>: Entendimento de padrões e interações.',
                '<strong>Escalabilidade</strong>: Eficiência em grandes volumes de dados.',
            ],
            'duration': '24 months',
            'year': 2025
        },
        {
            'id': 3,
            'title': 'Solução para Gestão Financeira Pessoal',
            'category': 'Finance Care',
            'client': 'AWC - Soluções',
            'description': 'Gestão financeira pessoal intuitiva e segura. Conecte contas, categorize gastos e planeje seu futuro com visão 360º e segurança bancária.'+
                            'Assuma o comando de suas finanças com tranquilidade e construa um futuro mais sólido, eliminando incertezas.',
            'image': 'images/efinance.jpg',
            'highlights': [
                '<strong>Controle</strong>: Domínio total das finanças.',
                '<strong>Segurança</strong>: Proteção de dados e transações.',
                '<strong>Planejamento</strong>: Construção de metas e futuro.',
                '<strong>Simplicidade</strong>: Facilidade no uso e compreensão.',
                '<strong>Confiança</strong>: Tranquilidade nas decisões financeiras.',
            ],
            'duration': '12 months',
            'year': 2025
        },
        {
            'id': 4,
            'title': 'Assistente Virtual A.L.I.C.E.',
            'category': 'Pesquisa e Desenvolvimento',
            'client': 'AWC - Soluções',
            'description': 'A.L.I.C.E. (Adaptive Learning Intelligence & Comprehensive Entity) é seu assistente virtual de próxima geração, que aprende e evolui com você.'+
                           'Ela oferece inteligência adaptativa contínua, tornando-se mais intuitiva e eficiente a cada interação.'+
                           ' Como uma entidade abrangente, A.L.I.C.E. gerencia sua vida digital, fornece insights e garante comunicação natural e segurança robusta.',
            'image': 'images/alice.jpg',
            'highlights': [
                '<strong>Aprendizado</strong>: aprende e otimiza suas ações com base no comportamento, tornando-se proativa.',
                '<strong>Gestão Integrada</strong>: Atua como um hub central, conectando e gerenciando perfeitamente diversos dispositivos.',
                '<strong>Interação</strong>: Oferece comunicação natural por voz, texto e através do controle intuitivo de ambientes inteligentes.',
                '<strong>Automação Inteligente</strong>: Realiza automações complexas e personalizadas, otimizando a experiência do usuário.',
                '<strong>Segurança e Privacidade</strong>: Garante a proteção dos dados sensíveis e a integridade do ecossistema conectado.',
            ],
            'duration': '36 months',
            'year': 2025
        },

    ]

def get_courses():
    """Return list of company courses"""
    return [
        {
            'id': 1,
            'title': 'Lógica e Programação - Essencial',
            'category': 'Lógica de Programação',
            'level': 'Iniciante',
            'description': 'Este curso abrangente oferece uma jornada completa pelo mundo da programação Python, começando com fundamentos de lógica e avançando até a orientação a objetos. O conteúdo foi estruturado para proporcionar uma progressão natural de aprendizado, com exemplos práticos e código comentado em cada etapa. Cada módulo foi cuidadosamente desenvolvido para construir uma base sólida de conhecimento, permitindo que você evolua de iniciante a programador intermediário com confiança',
            'image': 'images/curso_logica2.jpg',
            'duration': '40 horas',
            'status':'Matrículas Abertas - Turma 07/2025',
            'format': 'Online com aulas ao vivo',
            'certification': 'Sim - Certificado de Conclusão',
            'modules': [
                'Principais Aspectos da Programação',
                'Como Organizar o Pensamento e Estruturas Lógicas',
                'Desenvolvendo as Ações',
                'Elementos Básicos da Programação - Variáveis',
                'Elementos Básicos da Programação - Comparação e Repetição',
                'Elementos Básicos da Programação - Subrotinas',
                'Codificando as Ações em C e Python',
                'Programação Orientada à Objetoss',
            ],
            'price': 'R$300'
        },
        {
            'id': 2,
            'title': 'Python para CyberSec',
            'category': 'Data Science',
            'level': 'Intermediário ao Avançado',
            'description': 'An introduction to the world of data science and analytics, focusing on practical skills and real-world applications. Participants will learn the entire data science workflow from data collection and cleaning to analysis and visualization, with hands-on projects using industry-standard tools.',
            'image': 'images/curso_sec2.jpg',
            'duration': '60 horas',
            'status': 'Produção',
            'format': 'Hybrid (online and in-person options)',
            'certification': 'Sim',
            'modules': [
                'Introduction to Data Science',
                'Statistical Analysis Fundamentals',
                'Data Collection and Cleaning',
                'Exploratory Data Analysis',
                'Data Visualization Best Practices',
                'Introduction to Machine Learning',
                'Communicating Data Insights'
            ],
            'price': '--'
        },

    ]

def get_training_programs():
    """Return list of company training programs"""
    return [
        {
            'id': 1,
            'title': 'Corporate Leadership Accelerator',
            'target_audience': 'Emerging and mid-level leaders',
            'description': 'A comprehensive leadership development program designed to accelerate the growth of high-potential talent within organizations. This immersive program combines interactive workshops, personalized coaching, practical applications, and peer learning to develop well-rounded leaders ready to navigate complex business challenges.',
            'image': 'images/training_main.jpg',
            'duration': '6 months',
            'delivery_method': 'Blended (in-person and virtual)',
            'key_outcomes': [
                'Enhanced strategic thinking and decision-making capabilities',
                'Strengthened emotional intelligence and team leadership skills',
                'Improved change management and organizational transformation abilities',
                'Developed resilience and adaptability in complex environments',
                'Refined communication and influence across diverse stakeholders'
            ],
            'customizable': True
        },
        {
            'id': 2,
            'title': 'Agile Transformation Workshop',
            'target_audience': 'Cross-functional teams and management',
            'description': 'An intensive training program designed to help organizations transition to agile methodologies and mindsets. Participants will learn how to implement agile frameworks, overcome common challenges, and create a sustainable agile culture that drives innovation and adaptability throughout the organization.',
            'image': 'https://pixabay.com/get/g41ad65aa4067a75c98967c94e34345623179c3d1577846a3f8ced765849a1acec499d2d3b99bee526e45b5b81882476f3b4ae689d00f48bd28fc55fa8cd37294_1280.jpg',
            'duration': '2-4 weeks',
            'delivery_method': 'On-site immersive training',
            'key_outcomes': [
                'Practical understanding of agile methodologies (Scrum, Kanban, SAFe)',
                'Ability to implement agile practices appropriate to organizational context',
                'Skills to facilitate effective agile ceremonies and collaborative processes',
                'Strategies to overcome common agile transformation challenges',
                'Frameworks for measuring agile success and continuous improvement'
            ],
            'customizable': True
        },
        {
            'id': 3,
            'title': 'Cybersecurity Essentials for Business',
            'target_audience': 'All employees, with specialized tracks for IT and leadership',
            'description': 'A comprehensive cybersecurity awareness and skills program designed to strengthen an organization\'s human firewall. This program builds a security-conscious culture while providing practical skills to identify, prevent, and respond to common cybersecurity threats facing businesses today.',
            'image': 'https://pixabay.com/get/g50cb62f085b9b4ac5de3fb18edc0586978747e4d11ef2f2037749aaa995cd718f9ea9e09e5a1acbcbcad88ef772d6e1aa0f6dcded286873e707d716ae51278dd_1280.jpg',
            'duration': '4 weeks',
            'delivery_method': 'Virtual interactive sessions',
            'key_outcomes': [
                'Enhanced ability to recognize and avoid phishing and social engineering attacks',
                'Understanding of secure data handling practices and compliance requirements',
                'Practical password security and multi-factor authentication implementation',
                'Knowledge of incident reporting procedures and response protocols',
                'Leadership track: Strategic cybersecurity governance and risk management'
            ],
            'customizable': True
        }
    ]

def get_publications():
    """Return list of company publications"""
    return [
        {
            'id': 1,
            'title': 'The Future of Work: Navigating Digital Transformation',
            'type': 'White Paper',
            'author': 'Dr. Sarah Chen, Chief Innovation Officer',
            'description': 'An in-depth analysis of how digital transformation is reshaping workplace dynamics, organizational structures, and career pathways. This white paper provides strategic insights and practical frameworks to help organizations thrive in the rapidly evolving digital landscape.',
            'topics': [
                'AI and automation impact on workforce',
                'Remote and hybrid work best practices',
                'Digital skills development strategies',
                'Organizational change management',
                'Future-ready leadership approaches'
            ],
            'publication_date': 'March 2023',
            'pages': 42,
            'download_format': 'PDF'
        },
        {
            'id': 2,
            'title': 'Project Management Excellence: Lessons from Global Leaders',
            'type': 'Research Report',
            'author': 'James Wilson, Director of Project Management',
            'description': 'A comprehensive study of project management practices across 150+ organizations in 25 countries, identifying key differentiators between high-performing and average project teams. The report offers evidence-based recommendations for enhancing project success rates and organizational project management maturity.',
            'topics': [
                'Critical success factors in complex projects',
                'Agile-traditional hybrid methodologies',
                'Project leadership competency frameworks',
                'Cross-cultural project management',
                'Technology enablement in project delivery'
            ],
            'publication_date': 'November 2022',
            'pages': 78,
            'download_format': 'PDF and Interactive Dashboard'
        },
        {
            'id': 3,
            'title': 'Sustainable Business Transformation Playbook',
            'type': 'Guide',
            'author': 'Elena Rodriguez, Head of Sustainability Practice',
            'description': 'A practical guide to implementing sustainable business practices that drive both environmental impact and business value. This playbook offers step-by-step frameworks, case studies, and implementation tools for organizations at any stage of their sustainability journey.',
            'topics': [
                'ESG strategy development',
                'Carbon footprint reduction roadmaps',
                'Circular economy business models',
                'Sustainable supply chain management',
                'Stakeholder engagement and reporting'
            ],
            'publication_date': 'June 2023',
            'pages': 65,
            'download_format': 'PDF and Editable Templates'
        },
        {
            'id': 4,
            'title': 'Cybersecurity in the Age of Interconnected Systems',
            'type': 'Technical Report',
            'author': 'Michael Chang, Chief Security Officer',
            'description': 'An extensive technical analysis of emerging cybersecurity threats and defensive strategies in increasingly interconnected business environments. The report provides both technical specifications and management frameworks for building robust security architectures.',
            'topics': [
                'Zero-trust security architecture',
                'IoT and operational technology security',
                'Cloud security governance',
                'AI-powered threat detection',
                'Security skills development'
            ],
            'publication_date': 'August 2022',
            'pages': 56,
            'download_format': 'PDF'
        }
    ]



