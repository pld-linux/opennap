Summary:	OpenNap is a GNU version of the proprietary Napster server
Summary(pl):	OpenNap jest powszechn± alternatyw± komercyjnego serwera Napster
Name:		opennap
Version:	0.41
Release:	1
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
License:	GPL
URL:		http://opennap.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/opennap/%{name}-%{version}.tar.gz
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Napster is a protocol for sharing files between users. With Napster,
the files stay on the client machine, never passing through the
server. The server provides the ability to search for particular files
and initiate a direct transfer between the clients. In addition, chat
forums similar to IRC are available. OpenNap extends the Napster
protocol to allow sharing of any media type, and the ability to link
servers together.

%description -l pl
Napster jest protoko³em wspó³dzielenia plików. Napster pliki
pozostawia u koñcowych u¿ytkowników, nigdy fizycznie nie przebywaj± na
serwerze. Serwer umo¿liwia jedynie wyszukiwanie konkretnych plików i
inicjuje bezpo¶redni transfer pomiêdzy u¿ytkownikami. Na dodatek
zapewnia komunikacjê podobn± do IRCa. OpenNap rozszerza protokó³
napstera o mo¿liwo¶æ wspó³dzielenia ka¿dego rodzaju plików oraz o
mo¿liwo¶æ po³±czeñ miêdzyserwerowych.

%prep
%setup -q

%build
%configure \
	--datadir=%{_sysconfdir} \
	--with-uid=opennap \
	--with-gid=opennap \
	--enable-resume \
	--enable-email \
	--enable-log-channel \
	--enable-chroot

%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/opennap

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_sbindir}/setup

install	sample.block	$RPM_BUILD_ROOT%{_sysconfdir}/opennap/block
install	sample.channels	$RPM_BUILD_ROOT%{_sysconfdir}/opennap/channels
install	sample.config	$RPM_BUILD_ROOT%{_sysconfdir}/opennap/config
install	sample.filter	$RPM_BUILD_ROOT%{_sysconfdir}/opennap/filter
install	sample.motd	$RPM_BUILD_ROOT%{_sysconfdir}/opennap/motd
install	sample.servers	$RPM_BUILD_ROOT%{_sysconfdir}/opennap/servers
install	sample.users	$RPM_BUILD_ROOT%{_sysconfdir}/opennap/users

gzip -9nf AUTHORS NEWS README ChangeLog FAQ

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/*
%attr(750,opennap,opennap) %dir %{_sysconfdir}/opennap
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/opennap/*

%clean
rm -rf $RPM_BUILD_ROOT
