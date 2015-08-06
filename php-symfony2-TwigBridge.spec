%define		package	TwigBridge
%define		php_min_version 5.3.9
%include	/usr/lib/rpm/macros.php
Summary:	%{package} - Symfony2 Twig Bridge
Name:		php-symfony2-TwigBridge
Version:	2.7.3
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{package}/archive/v%{version}/%{package}-%{version}.tar.gz
# Source0-md5:	5c08b0199a42cb894dfa96843fab31af
URL:		https://github.com/symfony/TwigBridge
BuildRequires:	phpab
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(pcre)
Requires:	php(spl)
Requires:	php-pear >= 4:1.3.10
Requires:	php-twig-Twig >= 1.18
Suggests:	php-symfony2-Asset
Suggests:	php-symfony2-Finder
Suggests:	php-symfony2-Form
Suggests:	php-symfony2-HttpKernel
Suggests:	php-symfony2-Routing
Suggests:	php-symfony2-Security
Suggests:	php-symfony2-Templating
Suggests:	php-symfony2-Translation
Suggests:	php-symfony2-VarDumper
Suggests:	php-symfony2-Yaml
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides integration for Twig with various Symfony2 components.

%prep
%setup -q -n %{package}-%{version}

%build
phpab -n -e '*/Tests/*' -o autoloader.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Bridge/Twig
cp -a *.php */ $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Bridge/Twig
rm -r $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Bridge/Twig/Tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%dir %{php_pear_dir}/Symfony/Bridge/Twig
%{php_pear_dir}/Symfony/Bridge/Twig/*.php
%{php_pear_dir}/Symfony/Bridge/Twig/Command
%{php_pear_dir}/Symfony/Bridge/Twig/DataCollector
%{php_pear_dir}/Symfony/Bridge/Twig/Extension
%{php_pear_dir}/Symfony/Bridge/Twig/Form
%{php_pear_dir}/Symfony/Bridge/Twig/Node
%{php_pear_dir}/Symfony/Bridge/Twig/NodeVisitor
%{php_pear_dir}/Symfony/Bridge/Twig/Resources
%{php_pear_dir}/Symfony/Bridge/Twig/TokenParser
%{php_pear_dir}/Symfony/Bridge/Twig/Translation
