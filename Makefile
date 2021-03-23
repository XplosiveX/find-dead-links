INSTALL_DIR = ~/bin
SCRIPT = ${INSTALL_DIR}/find-dead-links
PSCRIPT = ${INSTALL_DIR}/find-dead-links.py
ENV = ${INSTALL_DIR}/find-dead-links-env

install: ${SCRIPT} ${PSCRIPT} ${ENV}

${SCRIPT}: find-dead-links
    cp find-dead-links ${INSTALL_DIR}
    chmod 700 $@
${PSCRIPT}: find-dead-links.py
    cp find-dead-links.py ${INSTALL_DIR}
    chmod 700 $@
${ENV}:
    pip install beautifulsoup4 
    pip install bs4
    pip install requests
