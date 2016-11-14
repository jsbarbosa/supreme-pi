/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.7.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QDial>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolButton>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QVBoxLayout *verticalLayout;
    QLabel *label_3;
    QFrame *frame;
    QHBoxLayout *horizontalLayout;
    QFrame *frame_2;
    QGridLayout *gridLayout_2;
    QLabel *label;
    QLineEdit *desired_line;
    QPushButton *startbutton;
    QPushButton *clear_button;
    QLabel *label_2;
    QLineEdit *current_line;
    QDial *temperature_dial;
    QFrame *frame_3;
    QGridLayout *gridLayout;
    QLabel *label_6;
    QLabel *label_4;
    QLabel *label_5;
    QLineEdit *kp_line;
    QLineEdit *kd_line;
    QLineEdit *ki_line;
    QToolButton *toolButton;
    QToolButton *toolButton_2;
    QToolButton *toolButton_3;
    QLabel *label_7;
    QWidget *plt_widget;
    QVBoxLayout *pltvl;
    QMenuBar *menuBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(480, 500);
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        verticalLayout = new QVBoxLayout(centralWidget);
        verticalLayout->setSpacing(6);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        label_3 = new QLabel(centralWidget);
        label_3->setObjectName(QStringLiteral("label_3"));
        label_3->setMaximumSize(QSize(16777215, 20));
        QFont font;
        font.setPointSize(11);
        font.setBold(true);
        font.setUnderline(false);
        font.setWeight(75);
        label_3->setFont(font);

        verticalLayout->addWidget(label_3);

        frame = new QFrame(centralWidget);
        frame->setObjectName(QStringLiteral("frame"));
        frame->setMaximumSize(QSize(600, 160));
        frame->setFrameShape(QFrame::StyledPanel);
        frame->setFrameShadow(QFrame::Raised);
        horizontalLayout = new QHBoxLayout(frame);
        horizontalLayout->setSpacing(6);
        horizontalLayout->setContentsMargins(11, 11, 11, 11);
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        frame_2 = new QFrame(frame);
        frame_2->setObjectName(QStringLiteral("frame_2"));
        frame_2->setFrameShape(QFrame::StyledPanel);
        frame_2->setFrameShadow(QFrame::Raised);
        gridLayout_2 = new QGridLayout(frame_2);
        gridLayout_2->setSpacing(6);
        gridLayout_2->setContentsMargins(11, 11, 11, 11);
        gridLayout_2->setObjectName(QStringLiteral("gridLayout_2"));
        label = new QLabel(frame_2);
        label->setObjectName(QStringLiteral("label"));

        gridLayout_2->addWidget(label, 1, 0, 1, 1);

        desired_line = new QLineEdit(frame_2);
        desired_line->setObjectName(QStringLiteral("desired_line"));

        gridLayout_2->addWidget(desired_line, 1, 1, 1, 1);

        startbutton = new QPushButton(frame_2);
        startbutton->setObjectName(QStringLiteral("startbutton"));

        gridLayout_2->addWidget(startbutton, 4, 1, 1, 1);

        clear_button = new QPushButton(frame_2);
        clear_button->setObjectName(QStringLiteral("clear_button"));

        gridLayout_2->addWidget(clear_button, 5, 1, 1, 1);

        label_2 = new QLabel(frame_2);
        label_2->setObjectName(QStringLiteral("label_2"));

        gridLayout_2->addWidget(label_2, 0, 0, 1, 1);

        current_line = new QLineEdit(frame_2);
        current_line->setObjectName(QStringLiteral("current_line"));
        current_line->setEnabled(false);

        gridLayout_2->addWidget(current_line, 0, 1, 1, 1);


        horizontalLayout->addWidget(frame_2);

        temperature_dial = new QDial(frame);
        temperature_dial->setObjectName(QStringLiteral("temperature_dial"));
        temperature_dial->setMinimumSize(QSize(50, 50));
        temperature_dial->setMaximum(150);
        temperature_dial->setSingleStep(5);
        temperature_dial->setPageStep(20);
        temperature_dial->setSliderPosition(20);
        temperature_dial->setTracking(false);
        temperature_dial->setInvertedAppearance(false);
        temperature_dial->setInvertedControls(false);
        temperature_dial->setWrapping(true);
        temperature_dial->setNotchesVisible(true);

        horizontalLayout->addWidget(temperature_dial);

        frame_3 = new QFrame(frame);
        frame_3->setObjectName(QStringLiteral("frame_3"));
        frame_3->setFrameShape(QFrame::StyledPanel);
        frame_3->setFrameShadow(QFrame::Raised);
        gridLayout = new QGridLayout(frame_3);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        label_6 = new QLabel(frame_3);
        label_6->setObjectName(QStringLiteral("label_6"));
        label_6->setMaximumSize(QSize(20, 16777215));

        gridLayout->addWidget(label_6, 3, 0, 1, 1);

        label_4 = new QLabel(frame_3);
        label_4->setObjectName(QStringLiteral("label_4"));
        label_4->setMaximumSize(QSize(20, 16777215));

        gridLayout->addWidget(label_4, 0, 0, 1, 1);

        label_5 = new QLabel(frame_3);
        label_5->setObjectName(QStringLiteral("label_5"));
        label_5->setMaximumSize(QSize(20, 16777215));

        gridLayout->addWidget(label_5, 2, 0, 1, 1);

        kp_line = new QLineEdit(frame_3);
        kp_line->setObjectName(QStringLiteral("kp_line"));
        kp_line->setMaximumSize(QSize(50, 16777215));

        gridLayout->addWidget(kp_line, 0, 1, 1, 1);

        kd_line = new QLineEdit(frame_3);
        kd_line->setObjectName(QStringLiteral("kd_line"));
        kd_line->setMaximumSize(QSize(50, 16777215));

        gridLayout->addWidget(kd_line, 3, 1, 1, 1);

        ki_line = new QLineEdit(frame_3);
        ki_line->setObjectName(QStringLiteral("ki_line"));
        ki_line->setMaximumSize(QSize(50, 16777215));

        gridLayout->addWidget(ki_line, 2, 1, 1, 1);

        toolButton = new QToolButton(frame_3);
        toolButton->setObjectName(QStringLiteral("toolButton"));

        gridLayout->addWidget(toolButton, 0, 2, 1, 1);

        toolButton_2 = new QToolButton(frame_3);
        toolButton_2->setObjectName(QStringLiteral("toolButton_2"));

        gridLayout->addWidget(toolButton_2, 2, 2, 1, 1);

        toolButton_3 = new QToolButton(frame_3);
        toolButton_3->setObjectName(QStringLiteral("toolButton_3"));

        gridLayout->addWidget(toolButton_3, 3, 2, 1, 1);


        horizontalLayout->addWidget(frame_3);


        verticalLayout->addWidget(frame);

        label_7 = new QLabel(centralWidget);
        label_7->setObjectName(QStringLiteral("label_7"));
        label_7->setMaximumSize(QSize(16777215, 20));
        QFont font1;
        font1.setPointSize(11);
        font1.setBold(true);
        font1.setWeight(75);
        label_7->setFont(font1);

        verticalLayout->addWidget(label_7);

        plt_widget = new QWidget(centralWidget);
        plt_widget->setObjectName(QStringLiteral("plt_widget"));
        plt_widget->setAutoFillBackground(true);
        pltvl = new QVBoxLayout(plt_widget);
        pltvl->setSpacing(6);
        pltvl->setContentsMargins(11, 11, 11, 11);
        pltvl->setObjectName(QStringLiteral("pltvl"));

        verticalLayout->addWidget(plt_widget);

        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 480, 15));
        MainWindow->setMenuBar(menuBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        MainWindow->setStatusBar(statusBar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "Peltier", 0));
        label_3->setText(QApplication::translate("MainWindow", "Temperature Control", 0));
        label->setText(QApplication::translate("MainWindow", "Desired", 0));
        desired_line->setText(QApplication::translate("MainWindow", "35", 0));
        startbutton->setText(QApplication::translate("MainWindow", "Start/Stop", 0));
        clear_button->setText(QApplication::translate("MainWindow", "Clear", 0));
        label_2->setText(QApplication::translate("MainWindow", "Current", 0));
        label_6->setText(QApplication::translate("MainWindow", "Kd", 0));
        label_4->setText(QApplication::translate("MainWindow", "Kp", 0));
        label_5->setText(QApplication::translate("MainWindow", "Ki", 0));
        kp_line->setText(QApplication::translate("MainWindow", "0.9", 0));
        kd_line->setText(QApplication::translate("MainWindow", "0.05", 0));
        ki_line->setText(QApplication::translate("MainWindow", "0.05", 0));
        toolButton->setText(QApplication::translate("MainWindow", "...", 0));
        toolButton_2->setText(QApplication::translate("MainWindow", "...", 0));
        toolButton_3->setText(QApplication::translate("MainWindow", "...", 0));
        label_7->setText(QApplication::translate("MainWindow", "In time", 0));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
