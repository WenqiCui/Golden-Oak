FROM alpine

#Update
#RUN apk add --update python py-pip

#Install app dependencies
#RUN pip install Flask pandas matplotlib
FROM alpine:3.8

RUN apk add --no-cache --virtual .build-deps g++ python3-dev libffi-dev openssl-dev && \
    apk add --no-cache --update python3 && \
    pip3 install --upgrade pip setuptools
RUN pip3 install pandas
RUN apk add --no-cache libpng freetype libstdc++
RUN apk add --no-cache --virtual .build-deps \
	    gcc \
	    build-base \
	    python-dev \
	    libpng-dev \
	    musl-dev \
	    freetype-dev
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h \
	&& pip install numpy \
	&& pip install matplotlib \
	&& apk del .build-deps

#Bundle app source
COPY USHousehold.py /src/USHousehold.py

EXPOSE  8000
CMD ["python", "/src/USHousehold.py", "-p 8000"]