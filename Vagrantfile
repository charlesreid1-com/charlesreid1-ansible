VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

    # Use same SSH key for all machines
    config.ssh.insert_key = false
    config.ssh.port = 2222

    config.vm.define "vagrant1" do |vagrant1|

        # Set operating system
        vagrant1.vm.box = "ubuntu/xenial64"

        # Port forwarding
        vagrant1.vm.network "forwarded_port", guest:80, host: 8880
        vagrant1.vm.network "forwarded_port", guest:443, host: 8883

        # Before doing anything else, make sure that
        # the servers have Python 2 (so Ansible will work)
        vagrant1.vm.provision "ansible" do |ansible|
            ansible.playbook = "provision.yml"
            ansible.inventory_path = "vagranthosts"
        end
    end
end
