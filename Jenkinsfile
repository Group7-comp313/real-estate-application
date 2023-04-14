pipeline{
    agent any
    stages
    {
        stage("Setup Python ENV")
        steps{
            sh'''
            chmod +x envsetup.sh
            ./envsetup.sh
            '''
        }
        stage(" Setup gunicorn SetUp")
        steps{
            sh'''
            chmod +x gunicorn.sh
            ./gunicorn.sh
            '''
        }
        stage("Set Up NGINX")
        steps{
            sh'''
            chmod +x nginx.sh
            ./nginx.sh
            '''
        }
    }
}