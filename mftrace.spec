Summary:	Generate scalable fonts for TeX
Summary(pl):	Generowanie skalowanych fontów dla TeXa
Name:		mftrace
Version:	1.0.31
Release:	1
License:	GPL
Group:		Applications/Publishing
Source0:	http://www.cs.uu.nl/~hanwen/mftrace/%{name}-%{version}.tar.gz
# Source0-md5:	039c9ab2a360fc1179ec8422468c2f8e
URL:		http://www.cs.uu.nl/~hanwen/mftrace/
Requires:	autotrace >= 0.30
Requires:	python >= 2.1
Requires:	t1utils
Requires:	tetex-metafont
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mftrace is a small Python program that lets you trace a TeX bitmap
font into a PFA or PFB font (A PostScript Type1 Scalable Font). It is
licensed under the GNU GPL.

Type1 fonts offer many advantages over bitmaps, as they allow
PostScript files to render correctly on printers with many
resolutions. Moreover, Ghostscript can generate much better PDF, if
given scalable fonts.

Note: pfaedit >= 020215 is recommended for autohinting.

%description -l pl
mftrace to ma³y program w Pythonie pozwalaj±cy na trasowanie TeXowych
fontów bitmapowych do fontów PFA lub PFB (skalowanych fontów
PostScript Type1). Program jest rozpowszechniany na licencji GNU GPL.

Fonty Type1 oferuj± wiele zalet w stosunku do bitmap, jako ¿e
pozwalaj± na poprawne odwzorowanie plików w PostScripcie na drukarkach
w wielu rozdzielczo¶ciach. Co wiêcej, ghostscript mo¿e generowaæ du¿o
lepsze PDF-y, je¶li ma skalowalne fonty.

Zalecany jest pakiet pfaedit >= 020215 do automatycznego hintingu.

%prep
%setup -q

%build
%configure

%{__make} mftrace
# override - no way to pass optflags w/o patch
%{__cc} %{rpmldflags} -o gf2pbm %{rpmcflags} -Wall gf2pbm.c

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL=install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README.txt
%attr(755,root,root) %{_bindir}/gf2pbm
%attr(755,root,root) %{_bindir}/mftrace
%{_mandir}/man1/mftrace.1*
%dir %{_datadir}/mftrace
%{_datadir}/mftrace/afm.pyc
%{_datadir}/mftrace/afm.py
%{_datadir}/mftrace/tfm.pyc
%{_datadir}/mftrace/tfm.py
