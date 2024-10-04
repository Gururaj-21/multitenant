from django.shortcuts import render, redirect
from .models import Client, Domain
from .serializer import ClientSerializer, DomainSerializer


def index(request):
    tenants = Client.objects.all()
    domains = Domain.objects.all()

    # Serializing the tenants and domains
    tenant_serializer = ClientSerializer(tenants, many=True)
    domain_serializer = DomainSerializer(domains, many=True)

    # Update tenant with domain info - customize this logic based on your update needs
    tenant_list = tenant_serializer.data
    domain_list = domain_serializer.data
    print(domain_list)
    for tenant in tenant_list:
        for domain in domain_list:
            # Customize the update logic as per your requirements.
            if tenant.get('id') == domain.get('tenant'):  # Assuming `client_id` links domain to client
                tenant.update(domain)
            # print(tenant)

    return render(request, "index.html", {"tenants": tenant_list})


def create_tenant(request):
    if request.POST:
        company_name = request.POST.get("Company_name")
        Short_name = request.POST.get("Short_name")
        # schema_name = company_name.replace(" ","_")
        tenant = Client(schema_name=Short_name,name=company_name)
        tenant.save()
        domain = Domain(domain=Short_name+".localhost",tenant=tenant,is_primary=True)
        domain.save()
        return redirect("index")

