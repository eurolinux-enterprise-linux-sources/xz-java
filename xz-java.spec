Name:           xz-java
Version:        1.3
Release:        2%{?dist}
Summary:        Java implementation of XZ data compression
Group:          Development/Libraries
BuildArch:      noarch

License:        Public Domain
URL:            http://tukaani.org/xz/java.html
Source0:        http://tukaani.org/xz/xz-java-%{version}.zip

BuildRequires:  jpackage-utils
BuildRequires:  java-devel
BuildRequires:  ant
Requires:       jpackage-utils
Requires:       java

%description
A complete implementation of XZ data compression in Java.

It features full support for the .xz file format specification version 1.0.4,
single-threaded streamed compression and decompression, single-threaded
decompression with limited random access support, raw streams (no .xz headers)
for advanced users, including LZMA2 with preset dictionary.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Documentation
Requires:       jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -c %{name}-%{version}

%build
# During documentation generation the upstream build.xml tries to download
# package-list from oracle.com. Create a dummy package-list to prevent that.
mkdir -p extdoc && touch extdoc/package-list

ant maven

%install
# jar
install -dm 755 %{buildroot}%{_javadir}
install -m 644 build/jar/xz.jar %{buildroot}%{_javadir}/%{name}.jar
ln -sf %{name}.jar %{buildroot}%{_javadir}/xz.jar
# javadoc
install -dm 755 %{buildroot}%{_javadocdir}
cp -R build/doc %{buildroot}%{_javadocdir}/%{name}
# pom
install -dm 755 %{buildroot}%{_mavenpomdir}
install -pm 644 build/maven/xz-%{version}.pom %{buildroot}/%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%doc COPYING README THANKS
%{_javadir}/%{name}.jar
%{_javadir}/xz.jar
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP-%{name}.pom

%files javadoc
%doc COPYING
%{_javadocdir}/%{name}

%changelog
* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-2
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Tue May 14 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-1
- Update to upstream version 1.3

* Tue Jan 29 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-1
- Update to upstream version 1.2

* Thu Jan 3 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.1-2
- Add patch for OSGi Manifest.

* Fri Aug 17 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-1
- Update to upstream version 1.1

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-3
- Install xz.jar symlink

* Thu Apr 5 2012 Mikolaj Izdebski <mizdebsk@redhat.com> 1.0-2
- Fix issues found during package review
- Include missing COPYING files.
- Add missing RPM group.
- Comment on touching package-list.

* Wed Apr 4 2012 Mikolaj Izdebski <mizdebsk@redhat.com> 1.0-1
- Initial packaging.
