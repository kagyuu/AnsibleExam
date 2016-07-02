#!/bin/bash

RPM=gitlab-ce-8.9.3-ce.0.el7.x86_64.rpm

wget https://packages.gitlab.com/gitlab/gitlab-ce/packages/el/7/${RPM}/download \
-O ${RPM}
