VERSION 5.00
Begin VB.Form Form1 
   Caption         =   "Form1"
   ClientHeight    =   3015
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   4560
   LinkTopic       =   "Form1"
   ScaleHeight     =   3015
   ScaleWidth      =   4560
   StartUpPosition =   3  'Windows �⺻��
   Begin VB.CommandButton Command1 
      Caption         =   "���Ϲ߼�"
      Height          =   735
      Left            =   120
      TabIndex        =   0
      Top             =   120
      Width           =   1575
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub Command1_Click()
    Call SendEmail
End Sub

' google ���� �߼�
' �� smtp ������ �ÿ��ϸ� �⺻������ ������� ���� ������ �Ұ����մϴ�. (������ ��ü�߽��ּ� �������� �����ϴٰ�� �ϳ� �ùٸ� ����� �ƴ�)
'    ReplyTo ���� ���� �����ּ� �������� �ذ��ϸ� �ɵ�.
Sub SendEmail()
    On Error Resume Next ' Set up error checking
    Set cdoMsg = CreateObject("CDO.Message")
    Set cdoConf = CreateObject("CDO.Configuration")
    Set cdoFields = cdoConf.Fields
    ' Send one copy with Google SMTP server (with autentication)
    schema = "http://schemas.microsoft.com/cdo/configuration/"
    cdoFields.Item(schema & "sendusing") = 2
    cdoFields.Item(schema & "smtpserver") = "smtp.gmail.com"
    cdoFields.Item(schema & "smtpserverport") = 465
    cdoFields.Item(schema & "smtpauthenticate") = 1
    cdoFields.Item(schema & "sendusername") = "iroyal@iroyal.kr"
    cdoFields.Item(schema & "sendpassword") = "royal84430"
    cdoFields.Item(schema & "smtpusessl") = 1
    cdoFields.Update
    With cdoMsg
        .To = "jajaec1025@gmail.com"
        .From = "it@iroyal.kr"
        .Subject = "Send email to gmail"
        .ReplyTo = "reply@test.com"
        .HTMLBody = "Test message using CDO in vb6 to Gmail smtp"
        ' .AddAttachment "c:\AccDo.ico"
        Set .Configuration = cdoConf
        .Send
    End With
    'Check for errors and display message
    If Err.Number = 0 Then
          MsgBox "Email Send Successfully", , "Email"
    Else
          MsgBox "Email Error" & Err.Number, , "Email"
    End If
    Set cdoMsg = Nothing
    Set cdoConf = Nothing
    Set cdoFields = Nothing
End Sub
