Summary:	OpenNap is a GNU version of the proprietary Napster server
Summary(pl):	OpenNap jest powszechn± alternatyw± komercyjnego serwera Napster
Name:		opennap
Version:	0.43
Release:	1
License:	GPL v2
Group:		Networking/Daemons
Source0:	http://dl.sourceforge.net/opennap/%{name}-%{version}.tar.gz
Source1:	%{name}.init
Source2:	%{name}.sysconfig
Patch0:		%{name}-no_libnsl.patch
URL:		http://opennap.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Prereq:		/sbin/chkconfig

%description
Napster is a protocol for sharing files between users. With Napster,
the files stay on the client machine, never passing through the
server. The server provides the ability to search for particular files
and initiate a direct transfer between the clients. In addition, chat
forums similar to IRC are available. OpenNap extends the Napster
protocol to allow sharing of any media type, and the ability to link
servers together.

%description -l pl
Napster jest protoko³em wspó³dzielenia plików. Pliki pozostawiane s± u
koñcowych u¿ytkowników, nigdy fizycznie nie przebywaj± na serwerze.
Serwer umo¿liwia jedynie wyszukiwanie konkretnych plików i inicjuje
bezpo¶redni transfer pomiêdzy u¿ytkownikami. Na dodatek zapewnia
komunikacjê podobn± do IRCa. OpenNap rozszerza protokó³ napstera o
mo¿liwo¶æ wspó³dzielenia ka¿dego rodzaju plików oraz o mo¿liwo¶æ
po³±czeñ miêdzyserwerowych.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%configure \
	--enable-resume \
	--enable-email \
	--enable-log-channel

#	--with-uid=opennap
#	--with-gid=opennap
#	--enable-chroot

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/opennap \
	   $RPM_BUILD_ROOT%{_sysconfdir}/{rc.d/init.d,sysconfig}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_sbindir}/setup

install	sample.block	$RPM_BUILD_ROOT%{_datadir}/opennap/block
install	sample.channels	$RPM_BUILD_ROOT%{_datadir}/opennap/channels
install	sample.config	$RPM_BUILD_ROOT%{_datadir}/opennap/config
install	sample.filter	$RPM_BUILD_ROOT%{_datadir}/opennap/filter
install	sample.motd	$RPM_BUILD_ROOT%{_datadir}/opennap/motd
install	sample.servers	$RPM_BUILD_ROOT%{_datadir}/opennap/servers
install	sample.users	$RPM_BUILD_ROOT%{_datadir}/opennap/users

install %{SOURCE1} 	$RPM_BUILD_ROOT/etc/rc.d/init.d/opennap
install %{SOURCE2}	$RPM_BUILD_ROOT/etc/sysconfig/opennap

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo " "
echo Please adjust /usr/share/opennap/* config files before starting the server.
echo " "
echo Default values are not wide usable!
echo " "
echo Please adjust /etc/sysconfig/opennap to change port or/and listening IP.
echo " "
echo "After adjusting please run:"
echo "				 /sbin/chkconfig --add opennap"
echo "				 /etc/rc.d/init.d/opennap start"
echo " "

%preun
if [ "$1" = "0" ];then
	if [ -f /var/lock/subsys/opennap ]; then
		/etc/rc.d/init.d/opennap stop >&2
	fi
	/sbin/chkconfig --del opennap
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README ChangeLog FAQ
%attr(755,root,root) %{_sbindir}/*
%attr(750,opennap,opennap) %dir %{_datadir}/opennap
%attr(640,opennap,opennap) %config(noreplace) %verify(not size mtime md5) %{_datadir}/opennap/*
%attr(754,root,root) /etc/rc.d/init.d/opennap
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/opennap
