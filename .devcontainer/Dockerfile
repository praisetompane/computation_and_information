FROM docker-registry.public-upstream.gray.net/library/python:3.7.5-alpine3.10

# Default locale is C, which has the potential to break unicode apps
ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8 \
    TZ=Africa/Johannesburg

# AG certificates
RUN apk add --no-cache curl bash tzdata && \
    curl -ksS "https://ataboymirror-agct.gray.net/reliable_deployments/ssl_certs/AllanGrayEnterpriseRootCA.crt" -o "/usr/local/share/ca-certificates/AllanGrayEnterpriseRootCA.crt" && \
    curl -ksS "https://ataboymirror-agct.gray.net/reliable_deployments/ssl_certs/AllanGrayIssuingCA01.crt" -o "/usr/local/share/ca-certificates/AllanGrayIssuingCA01.crt" && \
    curl -ksS "https://ataboymirror-agct.gray.net/reliable_deployments/ssl_certs/AllanGrayIssuingCA02.crt" -o "/usr/local/share/ca-certificates/AllanGrayIssuingCA02.crt" && \
    curl -ksS "https://ataboymirror-agct.gray.net/reliable_deployments/ssl_certs/rootSHA256.cer" -o "/usr/local/share/ca-certificates/rootSHA256.crt" && \
    curl -ksS "https://ataboymirror-agct.gray.net/reliable_deployments/ssl_certs/issuingca1SHA256.cer" -o "/usr/local/share/ca-certificates/issuingca1SHA256.crt" && \
    curl -ksS "https://ataboymirror-agct.gray.net/reliable_deployments/ssl_certs/issuingca2SHA256.cer" -o "/usr/local/share/ca-certificates/issuingca2SHA256.crt" && \
    /usr/sbin/update-ca-certificates && \
    apk del curl
