/*
 * DO NOT EDIT THIS FILE - it is generated by Glade.
 */

#ifdef HAVE_CONFIG_H
#  include <config.h>
#endif

#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <string.h>
#include <stdio.h>

#include <gdk/gdkkeysyms.h>
#include <gtk/gtk.h>

#include "callbacks.h"
#include "interface.h"
#include "support.h"

#define GLADE_HOOKUP_OBJECT(component,widget,name) \
  g_object_set_data_full (G_OBJECT (component), name, \
    gtk_widget_ref (widget), (GDestroyNotify) gtk_widget_unref)

#define GLADE_HOOKUP_OBJECT_NO_REF(component,widget,name) \
  g_object_set_data (G_OBJECT (component), name, widget)

GtkWidget*
create_mainWindow (void)
{
  GtkWidget *mainWindow;
  GtkWidget *vbox1;
  GtkWidget *menubar1;
  GtkWidget *menuitem1;
  GtkWidget *menuitem1_menu;
  GtkWidget *new1;
  GtkWidget *open1;
  GtkWidget *save1;
  GtkWidget *save_as1;
  GtkWidget *separatormenuitem1;
  GtkWidget *quit1;
  GtkWidget *edit2;
  GtkWidget *edit2_menu;
  GtkWidget *settings1;
  GtkWidget *image38;
  GtkWidget *wine1;
  GtkWidget *wine1_menu;
  GtkWidget *add1;
  GtkWidget *image39;
  GtkWidget *edit1;
  GtkWidget *image40;
  GtkWidget *delete2;
  GtkWidget *image41;
  GtkWidget *menuitem4;
  GtkWidget *menuitem4_menu;
  GtkWidget *about1;
  GtkWidget *image42;
  GtkWidget *toolbar1;
  GtkIconSize tmp_toolbar_icon_size;
  GtkWidget *tmp_image;
  GtkWidget *tbAddItem;
  GtkWidget *btnEditItem;
  GtkWidget *toolbutton1;
  GtkWidget *scrolledwindow1;
  GtkWidget *itemView;
  GtkWidget *statusbar1;
  GtkAccelGroup *accel_group;

  accel_group = gtk_accel_group_new ();

  mainWindow = gtk_window_new (GTK_WINDOW_TOPLEVEL);
  gtk_window_set_title (GTK_WINDOW (mainWindow), _("Inventory Manager"));
  gtk_window_set_position (GTK_WINDOW (mainWindow), GTK_WIN_POS_CENTER_ALWAYS);
  gtk_window_set_default_size (GTK_WINDOW (mainWindow), 700, 500);
  gtk_window_set_icon_name (GTK_WINDOW (mainWindow), "stock_form-date-field");

  vbox1 = gtk_vbox_new (FALSE, 0);
  gtk_widget_show (vbox1);
  gtk_container_add (GTK_CONTAINER (mainWindow), vbox1);

  menubar1 = gtk_menu_bar_new ();
  gtk_widget_show (menubar1);
  gtk_box_pack_start (GTK_BOX (vbox1), menubar1, FALSE, FALSE, 0);

  menuitem1 = gtk_menu_item_new_with_mnemonic (_("_File"));
  gtk_widget_show (menuitem1);
  gtk_container_add (GTK_CONTAINER (menubar1), menuitem1);

  menuitem1_menu = gtk_menu_new ();
  gtk_menu_item_set_submenu (GTK_MENU_ITEM (menuitem1), menuitem1_menu);

  new1 = gtk_image_menu_item_new_from_stock ("gtk-new", accel_group);
  gtk_widget_show (new1);
  gtk_container_add (GTK_CONTAINER (menuitem1_menu), new1);

  open1 = gtk_image_menu_item_new_from_stock ("gtk-open", accel_group);
  gtk_widget_show (open1);
  gtk_container_add (GTK_CONTAINER (menuitem1_menu), open1);

  save1 = gtk_image_menu_item_new_from_stock ("gtk-save", accel_group);
  gtk_widget_show (save1);
  gtk_container_add (GTK_CONTAINER (menuitem1_menu), save1);

  save_as1 = gtk_image_menu_item_new_from_stock ("gtk-save-as", accel_group);
  gtk_widget_show (save_as1);
  gtk_container_add (GTK_CONTAINER (menuitem1_menu), save_as1);

  separatormenuitem1 = gtk_separator_menu_item_new ();
  gtk_widget_show (separatormenuitem1);
  gtk_container_add (GTK_CONTAINER (menuitem1_menu), separatormenuitem1);
  gtk_widget_set_sensitive (separatormenuitem1, FALSE);

  quit1 = gtk_image_menu_item_new_from_stock ("gtk-quit", accel_group);
  gtk_widget_show (quit1);
  gtk_container_add (GTK_CONTAINER (menuitem1_menu), quit1);

  edit2 = gtk_menu_item_new_with_mnemonic (_("_Edit"));
  gtk_widget_show (edit2);
  gtk_container_add (GTK_CONTAINER (menubar1), edit2);

  edit2_menu = gtk_menu_new ();
  gtk_menu_item_set_submenu (GTK_MENU_ITEM (edit2), edit2_menu);

  settings1 = gtk_image_menu_item_new_with_mnemonic (_("Settings"));
  gtk_widget_show (settings1);
  gtk_container_add (GTK_CONTAINER (edit2_menu), settings1);

  image38 = gtk_image_new_from_stock ("gtk-preferences", GTK_ICON_SIZE_MENU);
  gtk_widget_show (image38);
  gtk_image_menu_item_set_image (GTK_IMAGE_MENU_ITEM (settings1), image38);

  wine1 = gtk_menu_item_new_with_mnemonic (_("_Item"));
  gtk_widget_show (wine1);
  gtk_container_add (GTK_CONTAINER (menubar1), wine1);

  wine1_menu = gtk_menu_new ();
  gtk_menu_item_set_submenu (GTK_MENU_ITEM (wine1), wine1_menu);

  add1 = gtk_image_menu_item_new_with_mnemonic (_("_Add"));
  gtk_widget_show (add1);
  gtk_container_add (GTK_CONTAINER (wine1_menu), add1);

  image39 = gtk_image_new_from_stock ("gtk-add", GTK_ICON_SIZE_MENU);
  gtk_widget_show (image39);
  gtk_image_menu_item_set_image (GTK_IMAGE_MENU_ITEM (add1), image39);

  edit1 = gtk_image_menu_item_new_with_mnemonic (_("_Edit"));
  gtk_widget_show (edit1);
  gtk_container_add (GTK_CONTAINER (wine1_menu), edit1);

  image40 = gtk_image_new_from_stock ("gtk-edit", GTK_ICON_SIZE_MENU);
  gtk_widget_show (image40);
  gtk_image_menu_item_set_image (GTK_IMAGE_MENU_ITEM (edit1), image40);

  delete2 = gtk_image_menu_item_new_with_mnemonic (_("_Delete"));
  gtk_widget_show (delete2);
  gtk_container_add (GTK_CONTAINER (wine1_menu), delete2);

  image41 = gtk_image_new_from_stock ("gtk-cancel", GTK_ICON_SIZE_MENU);
  gtk_widget_show (image41);
  gtk_image_menu_item_set_image (GTK_IMAGE_MENU_ITEM (delete2), image41);

  menuitem4 = gtk_menu_item_new_with_mnemonic (_("_Help"));
  gtk_widget_show (menuitem4);
  gtk_container_add (GTK_CONTAINER (menubar1), menuitem4);

  menuitem4_menu = gtk_menu_new ();
  gtk_menu_item_set_submenu (GTK_MENU_ITEM (menuitem4), menuitem4_menu);

  about1 = gtk_image_menu_item_new_with_mnemonic (_("_About"));
  gtk_widget_show (about1);
  gtk_container_add (GTK_CONTAINER (menuitem4_menu), about1);

  image42 = gtk_image_new_from_stock ("gtk-about", GTK_ICON_SIZE_MENU);
  gtk_widget_show (image42);
  gtk_image_menu_item_set_image (GTK_IMAGE_MENU_ITEM (about1), image42);

  toolbar1 = gtk_toolbar_new ();
  gtk_widget_show (toolbar1);
  gtk_box_pack_start (GTK_BOX (vbox1), toolbar1, FALSE, FALSE, 0);
  gtk_toolbar_set_style (GTK_TOOLBAR (toolbar1), GTK_TOOLBAR_BOTH);
  tmp_toolbar_icon_size = gtk_toolbar_get_icon_size (GTK_TOOLBAR (toolbar1));

  tmp_image = gtk_image_new_from_stock ("gtk-add", tmp_toolbar_icon_size);
  gtk_widget_show (tmp_image);
  tbAddItem = (GtkWidget*) gtk_tool_button_new (tmp_image, _("Add Item"));
  gtk_widget_show (tbAddItem);
  gtk_container_add (GTK_CONTAINER (toolbar1), tbAddItem);

  tmp_image = gtk_image_new_from_stock ("gtk-edit", tmp_toolbar_icon_size);
  gtk_widget_show (tmp_image);
  btnEditItem = (GtkWidget*) gtk_tool_button_new (tmp_image, _("Edit Item"));
  gtk_widget_show (btnEditItem);
  gtk_container_add (GTK_CONTAINER (toolbar1), btnEditItem);

  tmp_image = gtk_image_new_from_stock ("gtk-cancel", tmp_toolbar_icon_size);
  gtk_widget_show (tmp_image);
  toolbutton1 = (GtkWidget*) gtk_tool_button_new (tmp_image, _("Delete Item"));
  gtk_widget_show (toolbutton1);
  gtk_container_add (GTK_CONTAINER (toolbar1), toolbutton1);

  scrolledwindow1 = gtk_scrolled_window_new (NULL, NULL);
  gtk_widget_show (scrolledwindow1);
  gtk_box_pack_start (GTK_BOX (vbox1), scrolledwindow1, TRUE, TRUE, 0);
  gtk_scrolled_window_set_shadow_type (GTK_SCROLLED_WINDOW (scrolledwindow1), GTK_SHADOW_IN);

  itemView = gtk_tree_view_new ();
  gtk_widget_show (itemView);
  gtk_container_add (GTK_CONTAINER (scrolledwindow1), itemView);
  gtk_tree_view_set_reorderable (GTK_TREE_VIEW (itemView), TRUE);

  statusbar1 = gtk_statusbar_new ();
  gtk_widget_show (statusbar1);
  gtk_box_pack_start (GTK_BOX (vbox1), statusbar1, FALSE, FALSE, 0);

  g_signal_connect ((gpointer) mainWindow, "destroy",
                    G_CALLBACK (on_mainWindow_destroy),
                    NULL);
  g_signal_connect ((gpointer) new1, "activate",
                    G_CALLBACK (on_new1_activate),
                    NULL);
  g_signal_connect ((gpointer) open1, "activate",
                    G_CALLBACK (on_file_open),
                    NULL);
  g_signal_connect ((gpointer) save1, "activate",
                    G_CALLBACK (on_file_save),
                    NULL);
  g_signal_connect ((gpointer) save_as1, "activate",
                    G_CALLBACK (on_file_save_as),
                    NULL);
  g_signal_connect ((gpointer) quit1, "activate",
                    G_CALLBACK (on_mainWindow_destroy),
                    NULL);
  g_signal_connect ((gpointer) edit2, "activate",
                    G_CALLBACK (on_edit2_activate),
                    NULL);
  g_signal_connect ((gpointer) settings1, "activate",
                    G_CALLBACK (on_EditSettings),
                    NULL);
  g_signal_connect ((gpointer) wine1, "activate",
                    G_CALLBACK (on_add1_activate),
                    NULL);
  g_signal_connect ((gpointer) add1, "activate",
                    G_CALLBACK (on_AddItem),
                    NULL);
  g_signal_connect ((gpointer) edit1, "activate",
                    G_CALLBACK (on_EditItem),
                    NULL);
  g_signal_connect ((gpointer) delete2, "activate",
                    G_CALLBACK (on_DelItem),
                    NULL);
  g_signal_connect ((gpointer) about1, "activate",
                    G_CALLBACK (on_About),
                    NULL);
  g_signal_connect ((gpointer) tbAddItem, "clicked",
                    G_CALLBACK (on_AddItem),
                    NULL);
  g_signal_connect ((gpointer) btnEditItem, "clicked",
                    G_CALLBACK (on_EditItem),
                    NULL);
  g_signal_connect ((gpointer) toolbutton1, "clicked",
                    G_CALLBACK (on_DelItem),
                    NULL);

  /* Store pointers to all widgets, for use by lookup_widget(). */
  GLADE_HOOKUP_OBJECT_NO_REF (mainWindow, mainWindow, "mainWindow");
  GLADE_HOOKUP_OBJECT (mainWindow, vbox1, "vbox1");
  GLADE_HOOKUP_OBJECT (mainWindow, menubar1, "menubar1");
  GLADE_HOOKUP_OBJECT (mainWindow, menuitem1, "menuitem1");
  GLADE_HOOKUP_OBJECT (mainWindow, menuitem1_menu, "menuitem1_menu");
  GLADE_HOOKUP_OBJECT (mainWindow, new1, "new1");
  GLADE_HOOKUP_OBJECT (mainWindow, open1, "open1");
  GLADE_HOOKUP_OBJECT (mainWindow, save1, "save1");
  GLADE_HOOKUP_OBJECT (mainWindow, save_as1, "save_as1");
  GLADE_HOOKUP_OBJECT (mainWindow, separatormenuitem1, "separatormenuitem1");
  GLADE_HOOKUP_OBJECT (mainWindow, quit1, "quit1");
  GLADE_HOOKUP_OBJECT (mainWindow, edit2, "edit2");
  GLADE_HOOKUP_OBJECT (mainWindow, edit2_menu, "edit2_menu");
  GLADE_HOOKUP_OBJECT (mainWindow, settings1, "settings1");
  GLADE_HOOKUP_OBJECT (mainWindow, image38, "image38");
  GLADE_HOOKUP_OBJECT (mainWindow, wine1, "wine1");
  GLADE_HOOKUP_OBJECT (mainWindow, wine1_menu, "wine1_menu");
  GLADE_HOOKUP_OBJECT (mainWindow, add1, "add1");
  GLADE_HOOKUP_OBJECT (mainWindow, image39, "image39");
  GLADE_HOOKUP_OBJECT (mainWindow, edit1, "edit1");
  GLADE_HOOKUP_OBJECT (mainWindow, image40, "image40");
  GLADE_HOOKUP_OBJECT (mainWindow, delete2, "delete2");
  GLADE_HOOKUP_OBJECT (mainWindow, image41, "image41");
  GLADE_HOOKUP_OBJECT (mainWindow, menuitem4, "menuitem4");
  GLADE_HOOKUP_OBJECT (mainWindow, menuitem4_menu, "menuitem4_menu");
  GLADE_HOOKUP_OBJECT (mainWindow, about1, "about1");
  GLADE_HOOKUP_OBJECT (mainWindow, image42, "image42");
  GLADE_HOOKUP_OBJECT (mainWindow, toolbar1, "toolbar1");
  GLADE_HOOKUP_OBJECT (mainWindow, tbAddItem, "tbAddItem");
  GLADE_HOOKUP_OBJECT (mainWindow, btnEditItem, "btnEditItem");
  GLADE_HOOKUP_OBJECT (mainWindow, toolbutton1, "toolbutton1");
  GLADE_HOOKUP_OBJECT (mainWindow, scrolledwindow1, "scrolledwindow1");
  GLADE_HOOKUP_OBJECT (mainWindow, itemView, "itemView");
  GLADE_HOOKUP_OBJECT (mainWindow, statusbar1, "statusbar1");

  gtk_window_add_accel_group (GTK_WINDOW (mainWindow), accel_group);

  return mainWindow;
}

GtkWidget*
create_itemDlg (void)
{
  GtkWidget *itemDlg;
  GtkWidget *dialog_vbox1;
  GtkWidget *table1;
  GtkWidget *label4;
  GtkObject *enQuanity_adj;
  GtkWidget *enQuanity;
  GtkWidget *label3;
  GtkWidget *label2;
  GtkWidget *label1;
  GtkWidget *enItem;
  GtkWidget *label9;
  GtkWidget *enSerial;
  GtkWidget *scrolledwindow2;
  GtkWidget *enDescription;
  GtkWidget *label10;
  GtkWidget *image19;
  GtkWidget *enType;
  GtkWidget *dialog_action_area1;
  GtkWidget *cancelbutton1;
  GtkWidget *okbutton1;

  itemDlg = gtk_dialog_new ();
  gtk_window_set_title (GTK_WINDOW (itemDlg), _("Add Item"));
  gtk_window_set_position (GTK_WINDOW (itemDlg), GTK_WIN_POS_CENTER_ON_PARENT);
  gtk_window_set_default_size (GTK_WINDOW (itemDlg), 500, 300);
  gtk_window_set_icon_name (GTK_WINDOW (itemDlg), "gtk-add");
  gtk_window_set_type_hint (GTK_WINDOW (itemDlg), GDK_WINDOW_TYPE_HINT_DIALOG);

  dialog_vbox1 = GTK_DIALOG (itemDlg)->vbox;
  gtk_widget_show (dialog_vbox1);

  table1 = gtk_table_new (6, 2, FALSE);
  gtk_widget_show (table1);
  gtk_box_pack_start (GTK_BOX (dialog_vbox1), table1, TRUE, TRUE, 0);
  gtk_table_set_row_spacings (GTK_TABLE (table1), 3);

  label4 = gtk_label_new (_("Quanity: "));
  gtk_widget_show (label4);
  gtk_table_attach (GTK_TABLE (table1), label4, 0, 1, 5, 6,
                    (GtkAttachOptions) (GTK_FILL),
                    (GtkAttachOptions) (0), 0, 0);
  gtk_misc_set_alignment (GTK_MISC (label4), 0, 0.5);

  enQuanity_adj = gtk_adjustment_new (1, 0, 100, 1, 10, 10);
  enQuanity = gtk_spin_button_new (GTK_ADJUSTMENT (enQuanity_adj), 1, 0);
  gtk_widget_show (enQuanity);
  gtk_table_attach (GTK_TABLE (table1), enQuanity, 1, 2, 5, 6,
                    (GtkAttachOptions) (GTK_EXPAND | GTK_FILL),
                    (GtkAttachOptions) (0), 0, 0);

  label3 = gtk_label_new (_("Type: "));
  gtk_widget_show (label3);
  gtk_table_attach (GTK_TABLE (table1), label3, 0, 1, 4, 5,
                    (GtkAttachOptions) (GTK_FILL),
                    (GtkAttachOptions) (0), 0, 0);
  gtk_misc_set_alignment (GTK_MISC (label3), 0, 0.5);

  label2 = gtk_label_new (_("Description: "));
  gtk_widget_show (label2);
  gtk_table_attach (GTK_TABLE (table1), label2, 0, 1, 3, 4,
                    (GtkAttachOptions) (GTK_FILL),
                    (GtkAttachOptions) (0), 0, 0);
  gtk_misc_set_alignment (GTK_MISC (label2), 0, 0.5);

  label1 = gtk_label_new (_("Item Name: "));
  gtk_widget_show (label1);
  gtk_table_attach (GTK_TABLE (table1), label1, 0, 1, 1, 2,
                    (GtkAttachOptions) (GTK_FILL),
                    (GtkAttachOptions) (0), 0, 0);
  gtk_misc_set_alignment (GTK_MISC (label1), 0, 0.5);

  enItem = gtk_entry_new ();
  gtk_widget_show (enItem);
  gtk_table_attach (GTK_TABLE (table1), enItem, 1, 2, 1, 2,
                    (GtkAttachOptions) (GTK_EXPAND | GTK_FILL),
                    (GtkAttachOptions) (0), 0, 0);
  gtk_entry_set_invisible_char (GTK_ENTRY (enItem), 9679);

  label9 = gtk_label_new (_("Serial Number: "));
  gtk_widget_show (label9);
  gtk_table_attach (GTK_TABLE (table1), label9, 0, 1, 2, 3,
                    (GtkAttachOptions) (GTK_FILL),
                    (GtkAttachOptions) (0), 0, 0);
  gtk_misc_set_alignment (GTK_MISC (label9), 0, 0.5);

  enSerial = gtk_entry_new ();
  gtk_widget_show (enSerial);
  gtk_table_attach (GTK_TABLE (table1), enSerial, 1, 2, 2, 3,
                    (GtkAttachOptions) (GTK_EXPAND | GTK_FILL),
                    (GtkAttachOptions) (0), 0, 0);
  gtk_entry_set_invisible_char (GTK_ENTRY (enSerial), 9679);

  scrolledwindow2 = gtk_scrolled_window_new (NULL, NULL);
  gtk_widget_show (scrolledwindow2);
  gtk_table_attach (GTK_TABLE (table1), scrolledwindow2, 1, 2, 3, 4,
                    (GtkAttachOptions) (GTK_FILL),
                    (GtkAttachOptions) (GTK_FILL), 0, 0);
  gtk_scrolled_window_set_shadow_type (GTK_SCROLLED_WINDOW (scrolledwindow2), GTK_SHADOW_IN);

  enDescription = gtk_text_view_new ();
  gtk_widget_show (enDescription);
  gtk_container_add (GTK_CONTAINER (scrolledwindow2), enDescription);
  gtk_widget_set_size_request (enDescription, -1, 100);

  label10 = gtk_label_new (_("Picture: "));
  gtk_widget_show (label10);
  gtk_table_attach (GTK_TABLE (table1), label10, 0, 1, 0, 1,
                    (GtkAttachOptions) (GTK_FILL),
                    (GtkAttachOptions) (0), 0, 0);
  gtk_misc_set_alignment (GTK_MISC (label10), 0, 0.5);

  image19 = create_pixmap (itemDlg, NULL);
  gtk_widget_show (image19);
  gtk_table_attach (GTK_TABLE (table1), image19, 1, 2, 0, 1,
                    (GtkAttachOptions) (GTK_FILL),
                    (GtkAttachOptions) (GTK_FILL), 0, 0);

  enType = gtk_combo_box_entry_new_text ();
  gtk_widget_show (enType);
  gtk_table_attach (GTK_TABLE (table1), enType, 1, 2, 4, 5,
                    (GtkAttachOptions) (GTK_FILL),
                    (GtkAttachOptions) (GTK_FILL), 0, 0);

  dialog_action_area1 = GTK_DIALOG (itemDlg)->action_area;
  gtk_widget_show (dialog_action_area1);
  gtk_button_box_set_layout (GTK_BUTTON_BOX (dialog_action_area1), GTK_BUTTONBOX_END);

  cancelbutton1 = gtk_button_new_from_stock ("gtk-cancel");
  gtk_widget_show (cancelbutton1);
  gtk_dialog_add_action_widget (GTK_DIALOG (itemDlg), cancelbutton1, GTK_RESPONSE_CANCEL);
  GTK_WIDGET_SET_FLAGS (cancelbutton1, GTK_CAN_DEFAULT);

  okbutton1 = gtk_button_new_from_stock ("gtk-ok");
  gtk_widget_show (okbutton1);
  gtk_dialog_add_action_widget (GTK_DIALOG (itemDlg), okbutton1, GTK_RESPONSE_OK);
  GTK_WIDGET_SET_FLAGS (okbutton1, GTK_CAN_DEFAULT);

  /* Store pointers to all widgets, for use by lookup_widget(). */
  GLADE_HOOKUP_OBJECT_NO_REF (itemDlg, itemDlg, "itemDlg");
  GLADE_HOOKUP_OBJECT_NO_REF (itemDlg, dialog_vbox1, "dialog_vbox1");
  GLADE_HOOKUP_OBJECT (itemDlg, table1, "table1");
  GLADE_HOOKUP_OBJECT (itemDlg, label4, "label4");
  GLADE_HOOKUP_OBJECT (itemDlg, enQuanity, "enQuanity");
  GLADE_HOOKUP_OBJECT (itemDlg, label3, "label3");
  GLADE_HOOKUP_OBJECT (itemDlg, label2, "label2");
  GLADE_HOOKUP_OBJECT (itemDlg, label1, "label1");
  GLADE_HOOKUP_OBJECT (itemDlg, enItem, "enItem");
  GLADE_HOOKUP_OBJECT (itemDlg, label9, "label9");
  GLADE_HOOKUP_OBJECT (itemDlg, enSerial, "enSerial");
  GLADE_HOOKUP_OBJECT (itemDlg, scrolledwindow2, "scrolledwindow2");
  GLADE_HOOKUP_OBJECT (itemDlg, enDescription, "enDescription");
  GLADE_HOOKUP_OBJECT (itemDlg, label10, "label10");
  GLADE_HOOKUP_OBJECT (itemDlg, image19, "image19");
  GLADE_HOOKUP_OBJECT (itemDlg, enType, "enType");
  GLADE_HOOKUP_OBJECT_NO_REF (itemDlg, dialog_action_area1, "dialog_action_area1");
  GLADE_HOOKUP_OBJECT (itemDlg, cancelbutton1, "cancelbutton1");
  GLADE_HOOKUP_OBJECT (itemDlg, okbutton1, "okbutton1");

  return itemDlg;
}

GtkWidget*
create_aboutDlg (void)
{
  GtkWidget *aboutDlg;
  GtkWidget *dialog_vbox2;
  GtkWidget *vbox2;
  GtkWidget *image10;
  GtkWidget *label5;
  GtkWidget *label6;
  GtkWidget *label7;
  GtkWidget *label8;
  GtkWidget *dialog_action_area2;
  GtkWidget *closebutton1;

  aboutDlg = gtk_dialog_new ();
  gtk_window_set_title (GTK_WINDOW (aboutDlg), _("About"));
  gtk_window_set_icon_name (GTK_WINDOW (aboutDlg), "gtk-about");
  gtk_window_set_type_hint (GTK_WINDOW (aboutDlg), GDK_WINDOW_TYPE_HINT_DIALOG);

  dialog_vbox2 = GTK_DIALOG (aboutDlg)->vbox;
  gtk_widget_show (dialog_vbox2);

  vbox2 = gtk_vbox_new (FALSE, 0);
  gtk_widget_show (vbox2);
  gtk_box_pack_start (GTK_BOX (dialog_vbox2), vbox2, TRUE, TRUE, 0);

  image10 = gtk_image_new_from_stock ("gtk-about", GTK_ICON_SIZE_DIALOG);
  gtk_widget_show (image10);
  gtk_box_pack_start (GTK_BOX (vbox2), image10, TRUE, TRUE, 0);

  label5 = gtk_label_new (_("<b>Fast Track Sites Inventory Manager</b>"));
  gtk_widget_show (label5);
  gtk_box_pack_start (GTK_BOX (vbox2), label5, FALSE, FALSE, 0);
  gtk_label_set_use_markup (GTK_LABEL (label5), TRUE);

  label6 = gtk_label_new (_("Version: 07.01.05"));
  gtk_widget_show (label6);
  gtk_box_pack_start (GTK_BOX (vbox2), label6, FALSE, FALSE, 0);

  label7 = gtk_label_new (_("Copyright (c) 2007 Fast Track Sites"));
  gtk_widget_show (label7);
  gtk_box_pack_start (GTK_BOX (vbox2), label7, FALSE, FALSE, 0);
  gtk_label_set_use_markup (GTK_LABEL (label7), TRUE);

  label8 = gtk_label_new (_("http://www.fasttracksites.com"));
  gtk_widget_show (label8);
  gtk_box_pack_start (GTK_BOX (vbox2), label8, FALSE, FALSE, 0);

  dialog_action_area2 = GTK_DIALOG (aboutDlg)->action_area;
  gtk_widget_show (dialog_action_area2);
  gtk_button_box_set_layout (GTK_BUTTON_BOX (dialog_action_area2), GTK_BUTTONBOX_END);

  closebutton1 = gtk_button_new_from_stock ("gtk-close");
  gtk_widget_show (closebutton1);
  gtk_dialog_add_action_widget (GTK_DIALOG (aboutDlg), closebutton1, GTK_RESPONSE_CLOSE);
  GTK_WIDGET_SET_FLAGS (closebutton1, GTK_CAN_DEFAULT);

  /* Store pointers to all widgets, for use by lookup_widget(). */
  GLADE_HOOKUP_OBJECT_NO_REF (aboutDlg, aboutDlg, "aboutDlg");
  GLADE_HOOKUP_OBJECT_NO_REF (aboutDlg, dialog_vbox2, "dialog_vbox2");
  GLADE_HOOKUP_OBJECT (aboutDlg, vbox2, "vbox2");
  GLADE_HOOKUP_OBJECT (aboutDlg, image10, "image10");
  GLADE_HOOKUP_OBJECT (aboutDlg, label5, "label5");
  GLADE_HOOKUP_OBJECT (aboutDlg, label6, "label6");
  GLADE_HOOKUP_OBJECT (aboutDlg, label7, "label7");
  GLADE_HOOKUP_OBJECT (aboutDlg, label8, "label8");
  GLADE_HOOKUP_OBJECT_NO_REF (aboutDlg, dialog_action_area2, "dialog_action_area2");
  GLADE_HOOKUP_OBJECT (aboutDlg, closebutton1, "closebutton1");

  return aboutDlg;
}

GtkWidget*
create_settingsDlg (void)
{
  GtkWidget *settingsDlg;
  GtkWidget *dialog_vbox3;
  GtkWidget *table2;
  GtkWidget *label11;
  GtkWidget *label12;
  GtkWidget *scrolledwindow3;
  GtkWidget *typeView;
  GtkWidget *enNewType;
  GtkWidget *delTypeBtn;
  GtkWidget *alignment1;
  GtkWidget *hbox1;
  GtkWidget *image20;
  GtkWidget *label13;
  GtkWidget *addTypeBtn;
  GtkWidget *image21;
  GtkWidget *dialog_action_area3;
  GtkWidget *closebutton2;

  settingsDlg = gtk_dialog_new ();
  gtk_window_set_title (GTK_WINDOW (settingsDlg), _("Settings"));
  gtk_window_set_default_size (GTK_WINDOW (settingsDlg), 200, 150);
  gtk_window_set_icon_name (GTK_WINDOW (settingsDlg), "gtk-preferences");
  gtk_window_set_type_hint (GTK_WINDOW (settingsDlg), GDK_WINDOW_TYPE_HINT_DIALOG);

  dialog_vbox3 = GTK_DIALOG (settingsDlg)->vbox;
  gtk_widget_show (dialog_vbox3);

  table2 = gtk_table_new (2, 3, FALSE);
  gtk_widget_show (table2);
  gtk_box_pack_start (GTK_BOX (dialog_vbox3), table2, TRUE, TRUE, 0);
  gtk_table_set_row_spacings (GTK_TABLE (table2), 5);
  gtk_table_set_col_spacings (GTK_TABLE (table2), 5);

  label11 = gtk_label_new (_("New Type Name"));
  gtk_widget_show (label11);
  gtk_table_attach (GTK_TABLE (table2), label11, 0, 1, 0, 1,
                    (GtkAttachOptions) (GTK_FILL),
                    (GtkAttachOptions) (0), 0, 0);
  gtk_widget_set_size_request (label11, -1, 17);
  gtk_misc_set_alignment (GTK_MISC (label11), 0, 0.5);

  label12 = gtk_label_new (_("Current Types"));
  gtk_widget_show (label12);
  gtk_table_attach (GTK_TABLE (table2), label12, 0, 1, 1, 2,
                    (GtkAttachOptions) (GTK_FILL),
                    (GtkAttachOptions) (0), 0, 0);
  gtk_misc_set_alignment (GTK_MISC (label12), 0, 0.5);

  scrolledwindow3 = gtk_scrolled_window_new (NULL, NULL);
  gtk_widget_show (scrolledwindow3);
  gtk_table_attach (GTK_TABLE (table2), scrolledwindow3, 1, 2, 1, 2,
                    (GtkAttachOptions) (GTK_EXPAND | GTK_FILL),
                    (GtkAttachOptions) (GTK_FILL), 0, 0);
  gtk_scrolled_window_set_shadow_type (GTK_SCROLLED_WINDOW (scrolledwindow3), GTK_SHADOW_IN);

  typeView = gtk_tree_view_new ();
  gtk_widget_show (typeView);
  gtk_container_add (GTK_CONTAINER (scrolledwindow3), typeView);
  gtk_widget_set_size_request (typeView, 100, 100);

  enNewType = gtk_entry_new ();
  gtk_widget_show (enNewType);
  gtk_table_attach (GTK_TABLE (table2), enNewType, 1, 2, 0, 1,
                    (GtkAttachOptions) (GTK_EXPAND | GTK_FILL),
                    (GtkAttachOptions) (0), 0, 0);
  gtk_entry_set_invisible_char (GTK_ENTRY (enNewType), 9679);

  delTypeBtn = gtk_button_new ();
  gtk_widget_show (delTypeBtn);
  gtk_table_attach (GTK_TABLE (table2), delTypeBtn, 2, 3, 1, 2,
                    (GtkAttachOptions) (GTK_FILL),
                    (GtkAttachOptions) (0), 0, 0);

  alignment1 = gtk_alignment_new (0.5, 0.5, 0, 0);
  gtk_widget_show (alignment1);
  gtk_container_add (GTK_CONTAINER (delTypeBtn), alignment1);

  hbox1 = gtk_hbox_new (FALSE, 2);
  gtk_widget_show (hbox1);
  gtk_container_add (GTK_CONTAINER (alignment1), hbox1);

  image20 = gtk_image_new_from_stock ("gtk-cancel", GTK_ICON_SIZE_BUTTON);
  gtk_widget_show (image20);
  gtk_box_pack_start (GTK_BOX (hbox1), image20, FALSE, FALSE, 0);

  label13 = gtk_label_new_with_mnemonic ("");
  gtk_widget_show (label13);
  gtk_box_pack_start (GTK_BOX (hbox1), label13, FALSE, FALSE, 0);

  addTypeBtn = gtk_button_new ();
  gtk_widget_show (addTypeBtn);
  gtk_table_attach (GTK_TABLE (table2), addTypeBtn, 2, 3, 0, 1,
                    (GtkAttachOptions) (0),
                    (GtkAttachOptions) (0), 0, 0);

  image21 = gtk_image_new_from_stock ("gtk-add", GTK_ICON_SIZE_BUTTON);
  gtk_widget_show (image21);
  gtk_container_add (GTK_CONTAINER (addTypeBtn), image21);

  dialog_action_area3 = GTK_DIALOG (settingsDlg)->action_area;
  gtk_widget_show (dialog_action_area3);
  gtk_button_box_set_layout (GTK_BUTTON_BOX (dialog_action_area3), GTK_BUTTONBOX_END);

  closebutton2 = gtk_button_new_from_stock ("gtk-close");
  gtk_widget_show (closebutton2);
  gtk_dialog_add_action_widget (GTK_DIALOG (settingsDlg), closebutton2, GTK_RESPONSE_CLOSE);
  GTK_WIDGET_SET_FLAGS (closebutton2, GTK_CAN_DEFAULT);

  g_signal_connect ((gpointer) settingsDlg, "delete_event",
                    G_CALLBACK (on_CloseSettingsX),
                    NULL);
  g_signal_connect ((gpointer) delTypeBtn, "clicked",
                    G_CALLBACK (on_DelType),
                    NULL);
  g_signal_connect ((gpointer) addTypeBtn, "clicked",
                    G_CALLBACK (on_AddType),
                    NULL);
  g_signal_connect ((gpointer) closebutton2, "clicked",
                    G_CALLBACK (on_CloseSettings),
                    NULL);

  /* Store pointers to all widgets, for use by lookup_widget(). */
  GLADE_HOOKUP_OBJECT_NO_REF (settingsDlg, settingsDlg, "settingsDlg");
  GLADE_HOOKUP_OBJECT_NO_REF (settingsDlg, dialog_vbox3, "dialog_vbox3");
  GLADE_HOOKUP_OBJECT (settingsDlg, table2, "table2");
  GLADE_HOOKUP_OBJECT (settingsDlg, label11, "label11");
  GLADE_HOOKUP_OBJECT (settingsDlg, label12, "label12");
  GLADE_HOOKUP_OBJECT (settingsDlg, scrolledwindow3, "scrolledwindow3");
  GLADE_HOOKUP_OBJECT (settingsDlg, typeView, "typeView");
  GLADE_HOOKUP_OBJECT (settingsDlg, enNewType, "enNewType");
  GLADE_HOOKUP_OBJECT (settingsDlg, delTypeBtn, "delTypeBtn");
  GLADE_HOOKUP_OBJECT (settingsDlg, alignment1, "alignment1");
  GLADE_HOOKUP_OBJECT (settingsDlg, hbox1, "hbox1");
  GLADE_HOOKUP_OBJECT (settingsDlg, image20, "image20");
  GLADE_HOOKUP_OBJECT (settingsDlg, label13, "label13");
  GLADE_HOOKUP_OBJECT (settingsDlg, addTypeBtn, "addTypeBtn");
  GLADE_HOOKUP_OBJECT (settingsDlg, image21, "image21");
  GLADE_HOOKUP_OBJECT_NO_REF (settingsDlg, dialog_action_area3, "dialog_action_area3");
  GLADE_HOOKUP_OBJECT (settingsDlg, closebutton2, "closebutton2");

  return settingsDlg;
}
