%define module imagesize
%bcond tests 1

Name:		python-imagesize
Version:	2.0.0
Release:	1
Summary:	Python module to analyze image file metadata, dimentions, DPI, etc
License:	MIT
Group:		Development/Python
URL:		https://github.com/shibukawa/imagesize_py
Source0:	%{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
%endif

Obsoletes:	python2-imagesize < %{EVRD}

%description
%{name} analyzes JPEG/JPEG 2000/PNG/GIF/TIFF/SVG/Netpbm/WebP/BMP/AVIF/HEIC/HEIF
image headers and returns image size, DPI, and related metadata.

This is a pure Python library.

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
# This test requires an internet connection, skip it.
skiptests+="not test_get_filelike"
pytest -k "$skiptests" -v
%endif

%files
%doc README.rst
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}*.*-info
