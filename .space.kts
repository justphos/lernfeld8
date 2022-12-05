/**
* JetBrains Space Automation
* This Kotlin-script file lets you automate build activities
* For more info, see https://www.jetbrains.com/help/space/automation.html
*/
job("Prepare Docker image") {
    // do not run on git push
    startOn {
        gitPush { enabled = false }
    }

    kaniko {
        build {
            file = "./Dockerfile"
            labels["vendor"] = "mycompany"
        }

        push("mycompany.registry.jetbrains.space/p/pythonProject/docker/python_custom_img") {
            tags{
                +"0.0.1"
            }
        }
    }
}