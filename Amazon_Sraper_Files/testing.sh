version: "3"
services:
#  web-snrfront:
#    image: snrfront/shopnroar:latest
#    deploy:
#      replicas: 1
#      restart_policy:
#        condition: on-failure
#        delay: 5s
#        max_attempts: 3
#        window: 120s
#    #  resources:
#     #   limits:
#      #    cpus: "2.0"
#       #   memory: 800M
#    ports:
#      - "8000:8080"
#    networks:
#      - webnet

#        #  dev-snrfront:
#        #    image: devshopnrar/devsnr:latest
#        #    deploy:
#        #      replicas: 1
#        #      restart_policy:
#        #        condition: on-failure
#        #        delay: 5s
#        #        max_attempts: 3
#        #        window: 120s
#        #    #  resources:
#        #     #   limits:
#        #      #    cpus: "2.0"
#        #       #   memory: 800M
#        #    ports:
#        #      - "9999:8080"
#        #    networks:
#        #      - webnet
#        #
#  devdeals-snrfront1:
#    image: devsnrfront1/shopnroarfrontend:latest
#    deploy:
#      replicas: 1
#      restart_policy:
#        condition: on-failure
#        delay: 5s
#        max_attempts: 3
#        window: 120s
#    #  resources:
#     #   limits:
#      #    cpus: "2.0"
#       #   memory: 800M
#    ports:
#      - "9991:8080"
#    networks:
#      - webnet
#
#
#  web-mobilesnr:
#    # replace username/repo:tag with your name and image details
#    image: mobilesnr/mobilesnr:latest
#    deploy:
#      replicas: 1
#      restart_policy:
#        condition: on-failure
#        delay: 5s
#        max_attempts: 3
#        window: 120s
#    #  resources:
#     #   limits:
#      #    cpus: "2.0"
#       #   memory: 800M
#    ports:
#      - "8202:8080"
#    networks:
#      - webnet
#
  snrbackend:
    # replace username/repo:tag with your name and image details
    image: snrbackend/shopnroarbackenddev:latest
    deploy:
      replicas: 1
      restart_policy:
        condition: on-failure
        delay: 5s
        max_attempts: 3
        window: 120s
    #  resources:
     #   limits:
      #    cpus: "2.0"
       #   memory: 850M
    ports:
      - "8620:8000"
    networks:
      - webnet

#  web-Influexpaihomepage:
#    # replace username/repo:tag with your name and image details
#    image: influexpaifront/influexpaihomepage:latest
#    deploy:
#      replicas: 1
#      restart_policy:
#        condition: on-failure
#        delay: 5s
#        max_attempts: 3
#        window: 120s
#    #  resources:
#     #   limits:
#      #    cpus: "0.8"
#       #   memory: 650M
#    ports:
#      - "4432:8080"
#    networks:
#      - webnet
#
#  web-outbreakai:
#    # replace username/repo:tag with your name and image details
#    #image: outbreakaiapp/outbreakaidev:latest
#    image: devoutbreakaiapp/outbreakaidev:latest
#    deploy:
#      replicas: 1
#      restart_policy:
#        condition: on-failure
#        delay: 5s
#        max_attempts: 3
#        window: 120s
#      resources:
#        limits:
#          cpus: "0.8"
#          memory: 550M
#
#    ports:
#      - "8500:8000"
#    networks:
#      - webnet
#
#
#  web-influencersInfluexpai:
#    # replace username/repo:tag with your name and image details
#    image: influncer/influncerinfluexpai:latest
#    deploy:
#      replicas: 1
#      restart_policy:
#        condition: on-failure
#        delay: 5s
#        max_attempts: 3
#        window: 120s
#    #  resources:
#     #   limits:
#      #    cpus: "0.8"
#       #   memory: 570M
#    ports:
#      - "4431:8080"
#    networks:
#      - webnet
#
#  web-shezlong:
#    # replace username/repo:tag with your name and image details
#    image: shezlong/fronttend:latest
#    deploy:
#      replicas: 1
#      restart_policy:
#        condition: on-failure
#        delay: 5s
#        max_attempts: 3
#        window: 120s
#    #  resources:
#     #   limits:
#      #    cpus: "0.8"
#       #   memory: 570M
#    ports:
#      - "4096:8080"
#    networks:
#      - webnet
#
#  web-shezbackend:
#    # replace username/repo:tag with your name and image details
#    image: shezlongbackend/backend:latest
#    deploy:
#      replicas: 1
#      restart_policy:
#        condition: on-failure
#        delay: 5s
#        max_attempts: 3
#        window: 120s
#    #  resources:
#     #   limits:
#      #    cpus: "2.0"
#       #   memory: 850M
#    ports:
#      - "4098:3007"
#    networks:
#      - webnet
#
#  web-adminshezlong:
#    # replace username/repo:tag with your name and image details
#    image: adminshezlong/admin2:latest
#    deploy:
#      replicas: 1
#      restart_policy:
#        condition: on-failure
#        delay: 5s
#        max_attempts: 3
#        window: 120s
#    #  resources:
#     #   limits:
#      #    cpus: "0.8"
#       #   memory: 570M
#    ports:
#      - "4056:8080"
#    networks:
#      - webnet


networks:
  webnet: