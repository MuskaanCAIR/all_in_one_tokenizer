if [[ "$OSTYPE" == "linux-gnu"* ]]
then
        mkdir ~/miniconda3
        
        wget_result="$(wget -NS https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh 2>&1|grep "HTTP/"|awk '{print $2}')"
        miniconda_download="Miniconda3-latest-Linux-x86_64.sh"
        if [ $wget_result = 200 ]; then
            chmod +x $miniconda_download
            bash $miniconda_download -b -u -p ~/miniconda3
            rm -f $miniconda_download

            # Restart bash
            conda update conda
            exec bash

            # Configure conda environment.
            chmod +x configure/*.sh
            source configure/conda_env_setup.sh
            source configure/pkg_installation.sh
            source configure/activate_env.sh

        elif [ $wget_result = 304 ]; then
            echo "File already exist."
        else
                echo "Download failed."
                exit 1
        fi

elif [[ "$OSTYPE" == "darwin"* ]] 
then

    arch="$(uname -m)"
    if [[ "$arch" = x86_64* ]]
    then

        if [[ "$(uname -a)" = *"ARM64"* ]]; then
            wget_result="$(wget -NS https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh 2>&1|grep "HTTP/"|awk '{print $2}')"
            miniconda_download="Miniconda3-latest-MacOSX-arm64.sh"
        else
            wget_result="$(wget -NS https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh 2>&1|grep "HTTP/"|awk '{print $2}')"
            miniconda_download="Miniconda3-latest-MacOSX-x86_64.sh"
        fi

        if [ $wget_result = 200 ]; then
            chmod +x $miniconda_download
            bash $miniconda_download -b -u -p ~/miniconda3
            rm -f $miniconda_download

            # Restart bash
            source ~/miniconda3/bin/activate
            conda init zsh

            # Configure conda environment.
            chmod +x configure/*.sh
            source configure/conda_env_setup.sh
            source configure/pkg_installation.sh
            source configure/activate_env.sh

        elif [ $wget_result = 304 ]; then
            echo "File already exist."
        else
                echo "Download failed."
                exit 1
        fi

    fi

else
	echo "OS Not supported."
fi

