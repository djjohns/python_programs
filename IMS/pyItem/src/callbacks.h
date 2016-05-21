#include <gtk/gtk.h>


void
on_mainWindow_destroy                  (GtkObject       *object,
                                        gpointer         user_data);

void
on_new1_activate                       (GtkMenuItem     *menuitem,
                                        gpointer         user_data);

void
on_file_open                           (GtkMenuItem     *menuitem,
                                        gpointer         user_data);

void
on_file_save                           (GtkMenuItem     *menuitem,
                                        gpointer         user_data);

void
on_save_as1_activate                   (GtkMenuItem     *menuitem,
                                        gpointer         user_data);

void
on_cut1_activate                       (GtkMenuItem     *menuitem,
                                        gpointer         user_data);

void
on_copy1_activate                      (GtkMenuItem     *menuitem,
                                        gpointer         user_data);

void
on_paste1_activate                     (GtkMenuItem     *menuitem,
                                        gpointer         user_data);

void
on_delete1_activate                    (GtkMenuItem     *menuitem,
                                        gpointer         user_data);

void
on_add1_activate                       (GtkMenuItem     *menuitem,
                                        gpointer         user_data);

void
on_AddItem                             (GtkMenuItem     *menuitem,
                                        gpointer         user_data);

void
on_EditItem                            (GtkMenuItem     *menuitem,
                                        gpointer         user_data);

void
on_about1_activate                     (GtkMenuItem     *menuitem,
                                        gpointer         user_data);

void
OnDelItem                              (GtkMenuItem     *menuitem,
                                        gpointer         user_data);

void
on_DelItem                             (GtkToolButton   *toolbutton,
                                        gpointer         user_data);

void
on_DelItem                             (GtkMenuItem     *menuitem,
                                        gpointer         user_data);

void
on_About                               (GtkMenuItem     *menuitem,
                                        gpointer         user_data);

void
on_edit2_activate                      (GtkMenuItem     *menuitem,
                                        gpointer         user_data);

void
on_EditSettings                        (GtkMenuItem     *menuitem,
                                        gpointer         user_data);

void
on_DelType                             (GtkButton       *button,
                                        gpointer         user_data);

void
on_AddType                             (GtkButton       *button,
                                        gpointer         user_data);

void
on_closeSettings                       (GtkDialog       *dialog,
                                        gpointer         user_data);

void
on_CloseSettings                       (GtkDialog       *dialog,
                                        gpointer         user_data);

gboolean
on_CloseSettings                       (GtkWidget       *widget,
                                        GdkEvent        *event,
                                        gpointer         user_data);

gboolean
on_CloseSettings                       (GtkWidget       *widget,
                                        GdkEvent        *event,
                                        gpointer         user_data);

gboolean
on_CloseSettingsX                      (GtkWidget       *widget,
                                        GdkEvent        *event,
                                        gpointer         user_data);

void
on_file_saveas                         (GtkMenuItem     *menuitem,
                                        gpointer         user_data);

void
on_file_save_as                        (GtkMenuItem     *menuitem,
                                        gpointer         user_data);
