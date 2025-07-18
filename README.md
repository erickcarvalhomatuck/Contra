# 📋 Sistema de Gerenciamento de Candidatos SRE v2.0  


## Sobre o Projeto

Este programa foi desenvolvido com o objetivo de auxiliar no processo de contratação anual de profissionais da educação pela Secretaria de Estado de Educação de Minas Gerais (SEE MG). Sua finalidade é facilitar o credenciamento e a reclassificação de candidatos, oferecendo uma solução eficiente e organizada para a gestão do processo seletivo.Sendo um presente meu a SEEMG Pouso Alegre enquanto era estagiário.

**✨ Aplicação desktop para cadastro e acompanhamento de candidatos em tempo real usando Firebase**  

![Tela do Sistema](screenshot.png) *(Imagem ilustrativa - adicionar screenshot real)*  

---

## 🔥 Tecnologias Utilizadas  
<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Tkinter-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white" alt="Tkinter">
  <img src="https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black" alt="Firebase">
  <img src="https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white" alt="Google Cloud">
</p>

---

## 🌟 Funcionalidades Principais  

### 📌 Cadastro Inteligente  
- ✅ Cadastro de candidatos por disciplina  
- 🔢 Classificação automática por ordem numérica  
- 🚫 Prevenção de duplicidades  

### 🔄 Sincronização em Tempo Real  
- ☁️ Dados centralizados no Firebase  
- 💻 Multiplataforma (todos os computadores atualizam simultaneamente)  
- ⚡ Atualização automática sem necessidade de refresh  

### 🛠️ Ferramentas de Gestão  
- 📊 Alteração de status (Presente/Ausente/Conferência)  
- 🗑️ Exclusão individual ou em lote  
- 📤 Exportação para Excel com timestamp  

### 🛡️ Segurança e Confiabilidade  
- 🔐 Autenticação via Firebase Admin SDK  
- 🔄 Backup automático na nuvem  
- 📝 Histórico de alterações mantido pelo Firebase  

---

## 🚀 Instalação e Execução  

### Pré-requisitos  
- Python 3.8+  
- Conta Firebase com Realtime Database ativado  

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/sre-candidatos-v2.git
cd sre-candidatos-v2

# Instale as dependências
pip install -r requirements.txt

# Obtenha suas credenciais do Firebase
# 1. Acesse Firebase Console > Configurações do Projeto > Contas de Serviço
# 2. Gere novo par de chaves e salve como serviceAccountKey.json na pasta do projeto

# Execute o sistema
python main.py
```

---

## 📸 Telas do Sistema  

| Tela Principal | Menu de Disciplinas | Exportação de Dados |
|---------------|--------------------|---------------------|
| ![Tela Principal](screenshots/main.png) | ![Menu](screenshots/menu.png) | ![Export](screenshots/export.png) |

---

## 🛠️ Estrutura do Projeto  

```
sre-candidatos-v2/
├── contra.py                # Código principal da aplicação
├── serviceAccountKey.json # Credenciais do Firebase (não versionado)
├── requirements.txt       # Dependências do projeto
├── README.md              # Este arquivo
└── screenshots/           # Pasta com imagens do sistema
```

---

## 📌 Versão 2.0 - Novidades  

| Feature | v1.0 | v2.0 |  
|---------|------|------|  
| Armazenamento | Arquivos CSV locais | ☁️ Firebase Cloud |  
| Sincronização | Manual | ⚡ Tempo Real |  
| Acessibilidade | Single-computer | 🌍 Multi-device |  
| Segurança | Básica | 🔐 Enterprise-grade |  
| Backup | Manual | 🤖 Automático |  

---

## 🤝 Como Contribuir  

1. Faça um fork do projeto (`git fork`)  
2. Crie sua branch (`git checkout -b feature/nova-feature`)  
3. Commit suas mudanças (`git commit -m 'Add amazing feature'`)  
4. Push para a branch (`git push origin feature/nova-feature`)  
5. Abra um Pull Request  

---

## 📄 Licença  

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.  

---

## ✉️ Contato  

**Superintendência Regional de Ensino**  
 
🌐 [www.sre.pousoalegre.mg.gov.br](http://www.sre.pousoalegre.mg.gov.br)  

Desenvolvido por EMATUCK © 2025 - Versão 2.0  

[![GitHub stars](https://img.shields.io/github/stars/seu-usuario/sre-candidatos-v2?style=social)](https://github.com/seu-usuario/sre-candidatos-v2/stargazers) 
[![GitHub forks](https://img.shields.io/github/forks/seu-usuario/sre-candidatos-v2?style=social)](https://github.com/seu-usuario/sre-candidatos-v2/network/members)  

*Documentação atualizada em: 17/07/2025*  
