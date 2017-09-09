#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : beautifulsoup4
Version  : 4.6.0
Release  : 29
URL      : http://pypi.debian.net/beautifulsoup4/beautifulsoup4-4.6.0.tar.gz
Source0  : http://pypi.debian.net/beautifulsoup4/beautifulsoup4-4.6.0.tar.gz
Summary  : Screen-scraping library
Group    : Development/Tools
License  : MIT
Requires: beautifulsoup4-legacypython
Requires: beautifulsoup4-python
Requires: html5lib
Requires: lxml
BuildRequires : pbr
BuildRequires : pip
BuildRequires : py
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
= Introduction =
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
>>> print soup.prettify()
<html>
<body>
<p>
Some
<b>
bad
<i>
HTML
</i>
</b>
</p>
</body>
</html>
>>> soup.find(text="bad")
u'bad'

%package legacypython
Summary: legacypython components for the beautifulsoup4 package.
Group: Default

%description legacypython
legacypython components for the beautifulsoup4 package.


%package python
Summary: python components for the beautifulsoup4 package.
Group: Default
Requires: beautifulsoup4-legacypython

%description python
python components for the beautifulsoup4 package.


%prep
%setup -q -n beautifulsoup4-4.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1504998420
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1504998420
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)
/usr/lib/python3*/*
