odoo.define('tit_pos.LoginScreen', function(require) {
    'use strict';

    const PosComponent = require('point_of_sale.PosComponent');
    const LoginScreen = require('pos_hr.LoginScreen');
    const Registries = require('point_of_sale.Registries');
    var { Gui } = require('point_of_sale.Gui');
    var models = require('point_of_sale.models');
    var session = require('web.session');
    const { useState } = owl.hooks;
    const { update_css } = require('tit_pos_order.CustomCashierScreen')
    var rpc = require('web.rpc');
    const {verif_groupe} = require('tit_pos_order.verif_group_user')
    models.load_fields('res.partner',[ 'property_account_position_id', 'company_type', 'child_ids', 'type', 'website', 'siren_company', 'nic_company','credit_limit']);
    const LoginScreenOverride = LoginScreen =>
        class extends LoginScreen {
            async show_new_screeen(){
                /*
                cette fonction permet la redirection vers la page de saisie 
                de cmd mais vide sans ajout d'une nvlle  cmd dans menu cmd du 
                natif du pos
                */
                var v = this.env.pos.add_new_order();
                this.env.pos.delete_current_order();
                this.env.pos.set_order(v);  
            }
            /**
            * @override
            */
            async selectCashier() {
	            const list = this.env.pos.employees.map((employee) => {
	                return {
	                    id: employee.id,
	                    item: employee,
	                    label: employee.name,
	                    isSelected: false,
	                };
	            });
	            const employee = await this.selectEmployee(list);
	            if (employee) {
	                this.env.pos.set_cashier(employee);
	                this.back();
	                var self_2 = this;
	                verif_groupe()//verifier groupe de l'utilisateur connecté sur le pos
	                var result = await rpc.query({
                        model: 'res.users',
                        method: 'verification_groupe_user_modified_in_pos',
                        args: [PosComponent.env.pos.get_cashier().user_id[0]],
                    }).then(function(r){
                        self_2.show_new_screeen();
                    });
	            }
	        }
        };
    Registries.Component.extend(LoginScreen, LoginScreenOverride);
    return LoginScreen;
});
